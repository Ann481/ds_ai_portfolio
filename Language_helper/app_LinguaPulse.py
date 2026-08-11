import os, csv, io, tempfile, time
from datetime import datetime
from contextlib import contextmanager
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI
from sqlalchemy import create_engine, String, Text, Boolean, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column

# --- KONFIGURACJA I ENV ---
st.set_page_config(page_title="LinguaPulse", page_icon="🌍", layout="centered")
load_dotenv()

# --- SYSTEM LOGOWANIA ---
# Tutaj definiujesz prawidłowe dane logowania (możesz też pobierać je z .env)
USER_CREDENTIALS = {
    "admin": "haslo123",  # login: haslo
    "user": "tajne_haslo"
}

def login_form():
    st.title("🔐 Logowanie do LinguaPulse")
    
    with st.form("login_form"):
        username = st.text_input("Użytkownik")
        password = st.text_input("Hasło", type="password")
        submit_button = st.form_submit_button("Zaloguj się", use_container_width=True)
        
        if submit_button:
            if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
                st.session_state["authenticated"] = True
                st.session_state["username"] = username
                st.success("Zalogowano pomyślnie!")
                st.rerun()
            else:
                st.error("Nieprawidłowy użytkownik lub hasło")

# Sprawdzenie stanu logowania
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login_form()
    st.stop()  # Zatrzymuje wykonywanie reszty kodu dla niezalogowanych!

# --- KLIENT OPENAI ---
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    st.error("Brak OPENAI_API_KEY w pliku .env")
    st.stop()

@st.cache_resource
def get_openai_client():
    return OpenAI(api_key=OPENAI_API_KEY)

client = get_openai_client()

# --- BAZA DANYCH ---
DATABASE_URL = "sqlite:///language_ai.db"
Base = declarative_base()

@st.cache_resource
def get_database():
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
    Base.metadata.create_all(engine)
    return engine, sessionmaker(bind=engine)

engine, SessionLocal = get_database()

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class History(Base):
    __tablename__ = "history"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    operation: Mapped[str] = mapped_column(String(100), nullable=False)
    language: Mapped[str] = mapped_column(String(100), nullable=True)
    input_text: Mapped[str] = mapped_column(Text, nullable=False)
    output_text: Mapped[str] = mapped_column(Text, nullable=False)
    model: Mapped[str] = mapped_column(String(50), default="gpt-4o-mini")
    favorite: Mapped[bool] = mapped_column(Boolean, default=False)

# --- STAŁE I PROMPTY ---
PROMPTS = {
    "translation": "Jesteś profesjonalnym tłumaczem. Przetłumacz tekst z języka polskiego na język {language}. Zachowaj naturalny styl, kontekst i poprawność językową. Zwróć tylko tłumaczenie.",
    "correction": "Jesteś nauczycielem języka {language}. Przeanalizuj tekst ucznia.\n\nPrzygotuj:\n1. POPRAWIONA WERSJA:\n2. BŁĘDY:\n3. WYJAŚNIENIE (po polsku):\n4. PRZYKŁADY:",
    "message": "Jesteś profesjonalnym redaktorem języka {language}. Popraw wiadomość użytkownika.\nUwzględnij: gramatykę, styl, naturalność, dobór słów.\nStyl wiadomości: {style}\nNie zmieniaj znaczenia. Zwróć tylko poprawiony tekst.",
    "lesson": "Jesteś nauczycielem języka {language}. Przygotuj analizę tekstu.\nStruktura:\n1. Naturalne tłumaczenie.\n2. Ważne słowa i zwroty.\n3. Wyjaśnienie gramatyki.\n4. Wskazówki do nauki.\nOdpowiedz po polsku."
}

LANGUAGES = {
    "🇬🇧 Angielski": "angielski", "🇩🇪 Niemiecki": "niemiecki", "🇪🇸 Hiszpański": "hiszpański",
    "🇫🇷 Francuski": "francuski", "🇮🇹 Włoski": "włoski", "🇵🇹 Portugalski": "portugalski",
    "🇯🇵 Japoński": "japoński", "🇨🇳 Chiński": "chiński", "🇰🇷 Koreański": "koreański"
}

VOICE_OPTIONS = {
    "Nova - kobiecy": "nova", "Alloy - neutralny": "alloy", "Echo - męski": "echo",
    "Fable - narracyjny": "fable", "Onyx - głęboki": "onyx", "Shimmer - spokojny": "shimmer"
}

# Session State Initialization
for key, val in {"audio_text": None, "audio_file": None, "last_result": None, "selected_history": None}.items():
    if key not in st.session_state:
        st.session_state[key] = val

# --- HELPERY I LOGIKA BIZNESOWA ---
def save_history(operation, language, input_text, output_text, model="gpt-4o-mini"):
    with get_db() as db:
        record = History(operation=operation, language=language, input_text=input_text, output_text=output_text, model=model)
        db.add(record)
        db.commit()

def run_ai(operation, prompt_key, text, language, extra_data=None):
    start = time.time()
    prompt_tpl = PROMPTS[prompt_key]
    prompt = prompt_tpl.format(language=language, **(extra_data or {}))
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.3,
        messages=[{"role": "system", "content": prompt}, {"role": "user", "content": text}]
    )
    result = response.choices[0].message.content
    save_history(operation, language, text, result)
    return result, round(time.time() - start, 2)

def get_history(operation=None, language=None, search_text=None, favorite_only=False):
    with get_db() as db:
        q = db.query(History)
        if operation and operation != "Wszystkie": q = q.filter(History.operation == operation)
        if language and language != "Wszystkie": q = q.filter(History.language == language)
        if search_text: q = q.filter(History.input_text.contains(search_text))
        if favorite_only: q = q.filter(History.favorite == True)
        return q.order_by(History.created_at.desc()).all()

def toggle_favorite(history_id):
    with get_db() as db:
        item = db.query(History).filter(History.id == history_id).first()
        if item:
            item.favorite = not item.favorite
            db.commit()

def delete_history(history_id):
    with get_db() as db:
        item = db.query(History).filter(History.id == history_id).first()
        if item:
            db.delete(item)
            db.commit()

def get_history_statistics():
    with get_db() as db:
        return {
            "total": db.query(History).count(),
            "favorites": db.query(History).filter(History.favorite == True).count()
        }

def generate_audio(text, voice):
    try:
        speech_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        response = client.audio.speech.create(model="tts-1", voice=voice, input=text)
        speech_file.write(response.content)
        speech_file.close()
        return speech_file.name
    except Exception as e:
        st.error(f"Błąd generowania audio: {e}")
        return None

def export_history_csv():
    with get_db() as db:
        records = db.query(History).order_by(History.created_at.desc()).all()
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["Data", "Operacja", "Język", "Tekst wejściowy", "Wynik AI", "Model"])
        for r in records:
            writer.writerow([r.created_at, r.operation, r.language, r.input_text, r.output_text, r.model])
        return output.getvalue()

# --- SIDEBAR (HISTORIA I FILTRY + WYLOGOWANIE) ---
with st.sidebar:
    st.write(f"👤 Zalogowano jako: **{st.session_state['username']}**")
    if st.button("🚪 Wyloguj"):
        st.session_state["authenticated"] = False
        st.session_state["username"] = None
        st.rerun()

    st.divider()
    st.header("📜 Historia")
    stats = get_history_statistics()
    col_a, col_b = st.columns(2)
    col_a.metric("Wszystkie", stats["total"])
    col_b.metric("⭐ Ulubione", stats["favorites"])
    st.divider()
    
    op_filter = st.selectbox("Typ operacji", ["Wszystkie", "Tłumaczenie", "Korekta języka", "Profesjonalna wiadomość", "Wyjaśnienie słów i gramatyki"])
    lang_filter = st.selectbox("Język", ["Wszystkie"] + list(LANGUAGES.values()))
    search_txt = st.text_input("🔎 Szukaj")
    fav_only = st.checkbox("⭐ Tylko ulubione")
    
    st.divider()
    for item in get_history(op_filter, lang_filter, search_txt, fav_only)[:30]:
        title = f"{item.created_at.strftime('%d.%m.%Y %H:%M')} - {item.operation}"
        with st.expander(title):
            st.caption(f"Język: {item.language}")
            st.markdown("**Wejście:**")
            st.write(item.input_text[:300])
            st.markdown("**Wynik:**")
            st.write(item.output_text[:500])
            
            c1, c2, c3 = st.columns(3)
            if c1.button("📥", key=f"use_{item.id}", help="Użyj ponownie"):
                st.session_state.selected_history = item.input_text
                st.rerun()
            if c2.button("⭐" if item.favorite else "☆", key=f"fav_{item.id}"):
                toggle_favorite(item.id)
                st.rerun()
            if c3.button("🗑", key=f"del_{item.id}"):
                delete_history(item.id)
                st.rerun()

# --- GŁÓWNY INTERFEJS ---
st.title("🌍 LinguaPulse")
mode = st.radio("Wybierz funkcję:", ["🌐 Tłumaczenie", "📝 Korekta języka", "✨ Ładna wersja wiadomości", "📚 Wyjaśnienie słów i gramatyki"], horizontal=True)
st.divider()

col_lang, col_voice = st.columns(2)
target_language = LANGUAGES[col_lang.selectbox("🌍 Wybierz język:", list(LANGUAGES.keys()))]
voice = VOICE_OPTIONS[col_voice.selectbox("🔊 Wybierz głos:", list(VOICE_OPTIONS.keys()))]

if st.session_state.selected_history:
    st.info("📥 Załadowano tekst z historii")
    st.text_area("Załadowana treść:", st.session_state.selected_history, height=100)
    if st.button("❌ Zamknij podgląd"):
        st.session_state.selected_history = None
        st.rerun()

# Mapowanie operacji do konfiguracji UI
CONFIG = {
    "🌐 Tłumaczenie": ("Tłumaczenie", "translation", "Wpisz tekst po polsku:", "Np. Jutro jadę na wakacje z rodziną.", None),
    "📝 Korekta języka": ("Korekta języka", "correction", f"Wpisz tekst w języku {target_language}:", "Np. I have went to school yesterday.", None),
    "✨ Ładna wersja wiadomości": ("Profesjonalna wiadomość", "message", f"Wpisz wiadomość w języku {target_language}:", "Np. Hi, I want ask about your offer.", ["Formalny", "Biznesowy", "Przyjazny", "Codzienny", "Profesjonalny"]),
    "📚 Wyjaśnienie słów i gramatyki": ("Wyjaśnienie słów i gramatyki", "lesson", f"Wpisz tekst w języku {target_language}:", "Np. I have been learning English for two years.", None)
}

op_name, prompt_key, label, placeholder, styles = CONFIG[mode]
extra_data = {}

if styles:
    selected_style = st.selectbox("Styl wiadomości:", styles)
    extra_data["style"] = selected_style

text_input = st.text_area(label, height=180, placeholder=placeholder)

if st.button("🚀 Wykonaj", use_container_width=True):
    if not text_input.strip():
        st.warning("Wpisz tekst przed uruchomieniem.")
    else:
        with st.spinner("Przetwarzanie przez AI..."):
            res, duration = run_ai(op_name, prompt_key, text_input, target_language, extra_data)
            st.session_state.last_result = res
            st.session_state.audio_text = text_input if mode == "📚 Wyjaśnienie słów i gramatyki" else res
            st.session_state.audio_file = None
            st.success(f"Gotowe! ({duration}s)")
            st.markdown("### Wynik:")
            st.write(res)

# --- PANEL AUDIO & EKSPORT ---
st.divider()
st.subheader("🔊 Generator wymowy")

if st.session_state.audio_text:
    st.text_area("Tekst do audio:", st.session_state.audio_text, height=100)
    if st.button("🎧 Generuj audio", use_container_width=True):
        with st.spinner("Generowanie pliku audio..."):
            a_file = generate_audio(st.session_state.audio_text, voice)
            if a_file:
                st.session_state.audio_file = a_file
                st.success("Audio wygenerowane pomyślnie!")
    
    if st.session_state.audio_file:
        st.audio(st.session_state.audio_file, format="audio/mp3")
else:
    st.info("Wygeneruj tekst wyżej, aby móc stworzyć nagranie.")

st.divider()
st.subheader("📤 Eksport danych")

try:
    st.download_button("📜 Pobierz historię CSV", data=export_history_csv(), file_name="historia_tlumaczen.csv", mime="text/csv", use_container_width=True)
except Exception as err:
    st.error(f"Błąd eksportu: {err}")