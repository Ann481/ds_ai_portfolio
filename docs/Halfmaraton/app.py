import os
import io
import joblib
import boto3
import streamlit as st
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional

from openai import OpenAI

# 1. Bezpieczny import Langfuse (zapobiega awarii na App Platform)
try:
    from langfuse.decorators import observe
except ImportError:
    def observe(*args, **kwargs):
        def decorator(func):
            return func
        return decorator if args and callable(args[0]) else decorator

load_dotenv()

# 2. Konfiguracja klientów API
openai_client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# 3. Funkcja bezpiecznie ładująca model z DigitalOcean Spaces
@st.cache_resource
def load_model():
    model_dir = "models"
    model_filename = "halfmarathon_model.joblib"
    local_path = os.path.join(model_dir, model_filename)

    # Jeśli plik już istnieje lokalnie (np. po wcześniejszym pobraniu), użyj go
    if os.path.exists(local_path):
        return joblib.load(local_path)

    # Tworzymy folder, jeśli nie istnieje
    os.makedirs(model_dir, exist_ok=True)

    # Dane dostępowe do DO Spaces
    endpoint_url = os.environ.get("DO_SPACES_ENDPOINT")
    access_key = os.environ.get("DO_SPACES_KEY")
    secret_key = os.environ.get("DO_SPACES_SECRET")
    bucket_name = os.environ.get("DO_SPACES_BUCKET")

    if not all([endpoint_url, access_key, secret_key, bucket_name]):
        raise RuntimeError(
            "Brak pliku 'models/halfmarathon_model.joblib' oraz brak skonfigurowanych "
            "zmiennych środowiskowych DO_SPACES_* na App Platform!"
        )

    # Pobranie pliku modelu z DigitalOcean Spaces
    s3_client = boto3.client(
        's3',
        endpoint_url=endpoint_url,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )
    
    # Šcieżka do obiektu w Spaces (taka sama pod jaką zapisuje train_pipeline.py)
    remote_key = f"models/{model_filename}"
    s3_client.download_file(bucket_name, remote_key, local_path)

    return joblib.load(local_path)

model = load_model()

# 4. Schemat Pydantic do ekstrakcji danych przez LLM
class RunnerProfile(BaseModel):
    name: Optional[str] = Field(default=None, description="Imię użytkownika jeśli podano")
    gender: Optional[str] = Field(default=None, description="Płeć użytkownika: 'M' (mężczyzna) lub 'K' (kobieta)")
    age: Optional[int] = Field(default=None, description="Wiek w latach")
    time_5k_minutes: Optional[float] = Field(default=None, description="Czas na 5km przeliczony na pełne minuty (np. 22.5 dla 22:30)")
    missing_info: list[str] = Field(default_factory=list, description="Lista brakujących cech wybrana z: ['płeć', 'wiek', 'czas na 5km']")

@observe()
def extract_runner_data(user_text: str) -> RunnerProfile:
    """Wyciąga parametry biegacza z opisu tekstowego za pomocą OpenAI Structured Outputs."""
    system_prompt = """
    Jesteś asystentem Data Science. Twoim zadaniem jest wyciągnięcie danych ze swobodnej wypowiedzi biegacza:
    1. Płeć (K - kobieta, M - mężczyzna).
    2. Wiek (Liczba).
    3. Czas na 5 km (przeliczony na minuty w postaci dziesiętnej, np. 25 min 30 sek = 25.5).
    
    Jeśli brakuje którejś z powyższych informacji, dodaj odpowiednią nazwę do listy `missing_info`.
    """
    
    completion = openai_client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_text},
        ],
        response_format=RunnerProfile,
    )
    
    return completion.choices[0].message.parsed

def format_seconds(seconds: float) -> str:
    """Przekształca sekundy do formatu HH:MM:SS."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"

# 5. Interfejs Streamlit
st.set_page_config(page_title="Predyktor Półmaratonu", page_icon="🏃")

st.title("🏃 Estymator Czasu Półmaratonu")
st.write("Wpisz w polu poniżej krótką informację o sobie, np.: *Cześć, mam na imię Tomek, mam 30 lat i mój najlepszy czas na 5 km to 23 minuty 15 sekund.*")

user_input = st.text_area("Przedstaw się i podaj swoje parametry:", height=120)

if st.button("Szacuj czas półmaratonu", type="primary"):
    if not user_input.strip():
        st.warning("Proszę podać opis!")
    else:
        with st.spinner("LLM analizuje Twój wpis..."):
            extracted: RunnerProfile = extract_runner_data(user_input)
            
        # Sprawdzanie czy brakuje kluczowych danych
        if extracted.missing_info or not all([extracted.gender, extracted.age, extracted.time_5k_minutes]):
            st.error("❌ **Za mało danych do wyliczenia predykcji!**")
            missing_str = ", ".join(extracted.missing_info) if extracted.missing_info else "płeć, wiek lub czas na 5km"
            st.info(f"👉 Proszę uzupełnić brakujące informacje: **{missing_str}**")
        else:
            # Rozpoznanie i przygotowanie wektora cech
            is_male = 1 if extracted.gender.upper() == 'M' else 0
            age = extracted.age
            time_5k_sec = extracted.time_5k_minutes * 60.0

            # Predykcja
            prediction_sec = model.predict([[is_male, age, time_5k_sec]])[0]
            predicted_time_formatted = format_seconds(prediction_sec)
            
            st.success(f"Cześć **{extracted.name or 'Biegaczu'}**!")
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Wiek", f"{age} lat")
            col2.metric("Czas na 5km", f"{extracted.time_5k_minutes:.2f} min")
            col3.metric("Płeć", "Mężczyzna" if is_male else "Kobieta")

            st.markdown("---")
            st.subheader(f"⏱️ Przewidywany czas półmaratonu: **{predicted_time_formatted}**")
            
            # Wskaźnik tempa
            pace_sec_per_km = prediction_sec / 21.0975
            pace_min = int(pace_sec_per_km // 60)
            pace_sec = int(pace_sec_per_km % 60)
            st.caption(f"Średnie wymagane tempo: **{pace_min}:{pace_sec:02d} min/km**")