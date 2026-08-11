<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LinguaPulse – Pomagacz Językowy | Opis Projektu</title>
    <style>
        :root {
            --bg-light: #ffffff;
            --card-bg: #f8f9fa;
            --card-border: #e5e7eb;
            --primary-accent: #2563eb;
            --accent-green-bg: #dcfce7;
            --accent-green-text: #15803d;
            --text-main: #111827;
            --text-muted: #4b5563;
            --font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: var(--font-family);
            background-color: var(--bg-light);
            color: var(--text-main);
            line-height: 1.6;
            padding: 40px 20px;
        }

        .container {
            max-width: 900px;
            margin: 0 auto;
        }

        header {
            text-align: center;
            margin-bottom: 40px;
        }

        .logo {
            font-size: 2.5rem;
            font-weight: 800;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 12px;
            margin-bottom: 10px;
            color: var(--text-main);
        }

        header p {
            color: var(--text-muted);
            font-size: 1.15rem;
            max-width: 700px;
            margin: 0 auto;
        }

        .section-card {
            background-color: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 12px;
            padding: 28px;
            margin-bottom: 30px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        }

        .section-card h2 {
            font-size: 1.4rem;
            margin-bottom: 16px;
            color: #111827;
            border-bottom: 1px solid var(--card-border);
            padding-bottom: 10px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        /* Mockup Interfejsu LinguaPulse */
        .app-mockup {
            background-color: #ffffff;
            border: 1px solid var(--card-border);
            border-radius: 10px;
            padding: 24px;
            margin-top: 20px;
        }

        .radio-group {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            margin-bottom: 24px;
        }

        .radio-option {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.95rem;
            cursor: pointer;
            color: var(--text-main);
        }

        .radio-dot {
            width: 16px;
            height: 16px;
            border-radius: 50%;
            border: 2px solid #9ca3af;
            display: inline-block;
            position: relative;
        }

        .radio-option.active .radio-dot {
            border-color: var(--primary-accent);
            background-color: var(--primary-accent);
            box-shadow: inset 0 0 0 3px #ffffff;
        }

        .form-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-bottom: 20px;
        }

        .form-group label {
            display: block;
            font-size: 0.9rem;
            margin-bottom: 8px;
            color: var(--text-main);
            font-weight: 500;
        }

        .select-box, .textarea-box {
            width: 100%;
            background-color: #f3f4f6;
            border: 1px solid #d1d5db;
            border-radius: 6px;
            padding: 10px 14px;
            color: #111827;
            font-family: inherit;
            font-size: 0.95rem;
        }

        .textarea-box {
            height: 100px;
            resize: none;
            margin-bottom: 15px;
        }

        .btn-submit {
            width: 100%;
            background-color: #1f2937;
            border: 1px solid #1f2937;
            color: white;
            padding: 12px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 1rem;
            cursor: pointer;
            text-align: center;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }

        .status-badge {
            background-color: var(--accent-green-bg);
            border: 1px solid rgba(21, 128, 61, 0.2);
            color: var(--accent-green-text);
            padding: 10px 16px;
            border-radius: 6px;
            font-size: 0.9rem;
            font-weight: 600;
            margin-bottom: 20px;
        }

        .result-box {
            background-color: #f9fafb;
            border: 1px solid var(--card-border);
            border-radius: 8px;
            padding: 20px;
            margin-top: 15px;
            color: var(--text-main);
        }

        .result-box h3 {
            font-size: 1.2rem;
            margin-bottom: 12px;
            color: var(--text-main);
        }

        .explanation-list {
            margin-left: 20px;
            margin-bottom: 15px;
            color: var(--text-main);
        }

        .explanation-list li {
            margin-bottom: 6px;
        }

        .explanation-list ul {
            margin-left: 20px;
            margin-top: 6px;
        }

        /* Features List */
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 16px;
            margin-top: 15px;
        }

        .feature-card {
            background-color: #ffffff;
            padding: 18px;
            border-radius: 8px;
            border: 1px solid #e5e7eb;
        }

        .feature-card h3 {
            font-size: 1.05rem;
            margin-bottom: 8px;
            color: #111827;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .feature-card p {
            font-size: 0.88rem;
            color: var(--text-muted);
        }

        @media (max-width: 600px) {
            .form-row {
                grid-template-columns: 1fr;
            }
            .radio-group {
                flex-direction: column;
                gap: 12px;
            }
        }
    </style>
</head>
<body>

    <div class="container">

        <!-- HEADER -->
        <header>
            <div class="logo">🌏 LinguaPulse</div>
            <p>Pomagacz językowy – kompletne narzędzie do nauki języków obcych, tłumaczeń, analizy gramatycznej oraz generowania wymowy audio.</p>
        </header>

        <!-- OPIS GŁÓWNY -->
        <div class="section-card">
            <h2>📌 O projekcie</h2>
            <p>
                <strong>LinguaPulse</strong> to wszechstronny pomagacz językowy stworzony z myślą o efektywnej i przyjemnej nauce języków obcych.
                Aplikacja wykracza poza standardowe tłumaczenie słów i zdań – analizuje kontekst, poprawia błędy, dostosowuje styl wypowiedzi oraz szczegółowo wyjaśnia zawiłości gramatyczne wraz ze słownictwem i wskazówkami do nauki.
            </p>

            <div class="features-grid">
                <div class="feature-card">
                    <h3>🌐 Tłumaczenie</h3>
                    <p>Szybkie i precyzyjne przekładanie tekstów na wybrane języki obce.</p>
                </div>
                <div class="feature-card">
                    <h3>📝 Korekta języka</h3>
                    <p>Wykrywanie i poprawianie błędów ortograficznych, interpunkcyjnych i gramatycznych.</p>
                </div>
                <div class="feature-card">
                    <h3>✨ Ładna wersja</h3>
                    <p>Ulepszanie stylu i naturalności wypowiedzi dla lepszego brzmienia.</p>
                </div>
                <div class="feature-card">
                    <h3>📚 Wyjaśnienie słów & gramatyki</h3>
                    <p>Rozbicie zdania na czynniki pierwsze, słownik oraz objaśnienie reguł gramatycznych.</p>
                </div>
            </div>
        </div>

        <!-- PRZYKŁAD 1: TŁUMACZENIE I GENERATOR WYMOWY -->
        <div class="section-card">
            <h2>1. Tryb: Tłumaczenie + Generator Wymowy Audio</h2>
            <p>Użytkownik wybiera funkcję tłumaczenia, docelowy język oraz głos lektora, a następnie wpisuje tekst po polsku. Po wygenerowaniu wyniku dostępny jest również moduł syntezy mowy (TTS).</p>

            <div class="app-mockup">
                <div style="font-weight: 600; margin-bottom: 12px;">Wybierz funkcję:</div>
                <div class="radio-group">
                    <div class="radio-option active"><span class="radio-dot"></span> 🌐 Tłumaczenie</div>
                    <div class="radio-option"><span class="radio-dot"></span> 📝 Korekta języka</div>
                    <div class="radio-option"><span class="radio-dot"></span> ✨ Ładna wersja wiadomości</div>
                    <div class="radio-option"><span class="radio-dot"></span> 📚 Wyjaśnienie słów i gramatyki</div>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label>🌏 Wybierz język:</label>
                        <div class="select-box">ES Hiszpański</div>
                    </div>
                    <div class="form-group">
                        <label>🔊 Wybierz głos:</label>
                        <div class="select-box">Nova - kobiecy</div>
                    </div>
                </div>

                <div class="form-group">
                    <label>Wpisz tekst po polsku:</label>
                    <div class="textarea-box">Jak dojadę z lotniska do centrum Barcelony?</div>
                </div>

                <div class="btn-submit">🚀 Wykonaj</div>

                <div style="margin-top: 20px;">
                    <div class="status-badge">Gotowe! (2.54s)</div>
                    <div class="result-box">
                        <h3>Wynik:</h3>
                        <p style="font-size: 1.1rem; color: #111827; margin-bottom: 15px;">¿Cómo llego del aeropuerto al centro de Barcelona?</p>
                        
                        <div style="border-top: 1px solid var(--card-border); padding-top: 15px; margin-top: 15px;">
                            <h3 style="display: flex; align-items: center; gap: 8px;">🔊 Generator wymowy</h3>
                            <label style="font-size: 0.85rem; color: var(--text-muted); display: block; margin: 8px 0 4px 0;">Tekst do audio:</label>
                            <div class="textarea-box" style="height: 50px; margin-bottom: 10px;">¿Cómo llego del aeropuerto al centro de Barcelona?</div>
                            <div class="btn-submit">🎧 Generuj audio</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- PRZYKŁAD 2: WYJAŚNIENIE SŁÓW I GRAMATYKI -->
        <div class="section-card">
            <h2>2. Tryb: Wyjaśnienie Słów i Gramatyki</h2>
            <p>Aplikacja tworzy ustrukturyzowany raport edukacyjny zawierający naturalne tłumaczenie, kluczowe słownictwo z definicjami, zasady gramatyczne oraz praktyczne wskazówki do nauki.</p>

            <div class="app-mockup">
                <div style="font-weight: 600; margin-bottom: 12px;">Wybierz funkcję:</div>
                <div class="radio-group">
                    <div class="radio-option"><span class="radio-dot"></span> 🌐 Tłumaczenie</div>
                    <div class="radio-option"><span class="radio-dot"></span> 📝 Korekta języka</div>
                    <div class="radio-option"><span class="radio-dot"></span> ✨ Ładna wersja wiadomości</div>
                    <div class="radio-option active"><span class="radio-dot"></span> 📚 Wyjaśnienie słów i gramatyki</div>
                </div>

                <div class="result-box">
                    <h3>Wynik:</h3>
                    <ol class="explanation-list">
                        <li><strong>Naturalne tłumaczenie:</strong> "Jak dojdę z lotniska do centrum Barcelony?"</li>
                        <li><strong>Ważne słowa i zwroty:</strong>
                            <ul>
                                <li><strong>aeropuerto</strong> - lotnisko</li>
                                <li><strong>centro</strong> - centrum</li>
                                <li><strong>llego</strong> - przybywam, docieram (forma czasownika "llegar")</li>
                                <li><strong>cómo</strong> - jak</li>
                                <li><strong>del</strong> - z (połączenie "de" i "el", oznaczające "z" i "ten")</li>
                            </ul>
                        </li>
                        <li><strong>Wyjaśnienie gramatyki:</strong>
                            <ul>
                                <li>Czasownik "llegar" jest czasownikiem regularnym w języku hiszpańskim, co oznacza, że jego odmiana w czasie teraźniejszym jest zgodna z regularnymi wzorcami. W pierwszej osobie liczby pojedynczej (yo) przyjmuje formę "llego".</li>
                                <li>Użycie "del" (z + el) jest typowe w języku hiszpańskim, gdzie "de" oznacza "z", a "el" to rodzajnik męski "ten". W kontekście pytania oznacza to, że pytający chce wiedzieć, jak dotrzeć z konkretnego miejsca (lotniska) do innego (centrum).</li>
                            </ul>
                        </li>
                        <li><strong>Wskazówki do nauki:</strong>
                            <ul>
                                <li>Ćwicz używanie pytania "¿Cómo...?" w różnych kontekstach, aby stać się bardziej biegłym w zadawaniu pytań.</li>
                                <li>Ucz się słownictwa powiązanego z podróżami, aby móc swobodnie komunikować się w sytuacjach związanych z transportem.</li>
                                <li>Praktykuj odmianę czasowników regularnych, aby zrozumieć, jak działają w różnych czasach i osobach.</li>
                                <li>Spróbuj stworzyć własne zdania z użyciem nowych słów i zwrotów, aby utrwalić materiał.</li>
                            </ul>
                        </li>
                    </ol>
                </div>
            </div>
        </div>

        <footer>
            <p style="text-align: center; color: var(--text-muted); font-size: 0.85rem; margin-top: 30px; border-top: 1px solid var(--card-border); padding-top: 20px;">
                Projekt LinguaPulse • Pomagacz Językowy oparty na sztucznej inteligencji
            </p>
        </footer>

    </div>

</body>
</html>
