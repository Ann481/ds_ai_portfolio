<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Estymator Czasu Półmaratonu – Jak to działa?</title>
    <style>
        :root {
            --bg-light: #ffffff;
            --card-bg: #f8f9fa;
            --card-border: #e5e7eb;
            --primary-red: #dc2626;
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
            max-width: 800px;
            margin: 0 auto;
        }

        header {
            text-align: center;
            margin-bottom: 40px;
        }

        header h1 {
            font-size: 2.2rem;
            font-weight: 700;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 12px;
            color: var(--text-main);
        }

        header p {
            color: var(--text-muted);
            font-size: 1.1rem;
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
            font-size: 1.3rem;
            margin-bottom: 16px;
            color: #111827;
            border-bottom: 1px solid var(--card-border);
            padding-bottom: 10px;
        }

        /* Mockup UI Elements */
        .ui-mockup {
            background-color: #ffffff;
            border: 1px solid var(--card-border);
            border-radius: 8px;
            padding: 20px;
            margin-top: 15px;
        }

        .ui-label {
            font-size: 0.95rem;
            font-weight: 600;
            margin-bottom: 8px;
            color: #111827;
        }

        .ui-hint {
            font-style: italic;
            color: var(--text-muted);
            font-size: 0.9rem;
            margin-bottom: 12px;
        }

        .ui-textarea {
            width: 100%;
            height: 90px;
            background-color: #f3f4f6;
            border: 1px solid #d1d5db;
            border-radius: 6px;
            padding: 12px;
            color: #111827;
            font-family: inherit;
            font-size: 0.95rem;
            resize: none;
            margin-bottom: 15px;
        }

        .ui-button {
            background-color: var(--primary-red);
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 0.95rem;
            cursor: pointer;
            display: inline-block;
        }

        .ui-greeting {
            background-color: var(--accent-green-bg);
            border: 1px solid rgba(21, 128, 61, 0.2);
            color: var(--accent-green-text);
            padding: 14px 18px;
            border-radius: 6px;
            font-size: 1.1rem;
            font-weight: 600;
            margin-top: 15px;
            margin-bottom: 20px;
        }

        .extracted-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 15px;
            margin-top: 15px;
        }

        .extracted-item {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 6px;
            border: 1px solid #e5e7eb;
        }

        .extracted-item .label {
            font-size: 0.8rem;
            color: var(--text-muted);
            margin-bottom: 6px;
        }

        .extracted-item .val {
            font-size: 1.6rem;
            font-weight: 700;
            color: #111827;
        }

        .result-panel {
            margin-top: 20px;
            padding-top: 15px;
            border-top: 1px solid var(--card-border);
        }

        .result-header {
            font-size: 1.5rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 10px;
            color: #111827;
        }

        .result-sub {
            color: var(--text-muted);
            font-size: 0.9rem;
            margin-top: 6px;
        }

        /* Responsive */
        @media (max-width: 600px) {
            .extracted-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>

    <div class="container">

        <header>
            <h1>🏃 Estymator Czasu Półmaratonu</h1>
            <p>Aplikacja ML + OpenAI oparta na wprowadzaniu danych w języku naturalnym</p>
        </header>

        <!-- KROK 1 -->
        <div class="section-card">
            <h2>1. Wprowadzanie danych w języku naturalnym</h2>
            <p>Użytkownik nie wypełnia formularzy ani rozwijanych list. Wystarczy wpisać krótką informację o sobie w jednym polu tekstowym.</p>
            
            <div class="ui-mockup">
                <div class="ui-label">Przedstaw się i podaj swoje parametry:</div>
                <div class="ui-hint">Wpisz w polu poniżej krótką informację o sobie, np.: <i>Cześć, mam na imię Tomek, mam 30 lat i mój najlepszy czas na 5 km to 23 minuty 15 sekund.</i></div>
                <div class="ui-textarea" style="color: #6b7280;">Wpisz tutaj swoją wypowiedź...</div>
                <div class="ui-button">Szacuj czas półmaratonu</div>
            </div>
        </div>

        <!-- KROK 2 -->
        <div class="section-card">
            <h2>2. Wyłuskiwanie parametrów przez OpenAI</h2>
            <p>Model OpenAI (LLM) analizuje potoczny tekst i automatycznie wyciąga kluczowe dane: <strong>imię, wiek, czas na 5 km (tempo) oraz płeć</strong>.</p>
            
            <div class="ui-mockup">
                <div class="ui-label">Przedstaw się i podaj swoje parametry:</div>
                <div class="ui-textarea">Cześć, mam na imię Adrian, mam 35 lat i mój najlepszy czas na 5 km to 25 minut.</div>
                <div class="ui-button">Szacuj czas półmaratonu</div>

                <div class="ui-greeting">Cześć Adrian!</div>

                <div class="extracted-grid">
                    <div class="extracted-item">
                        <div class="label">Wiek</div>
                        <div class="val">35 lat</div>
                    </div>
                    <div class="extracted-item">
                        <div class="label">Czas na 5km</div>
                        <div class="val">25.00 min</div>
                    </div>
                    <div class="extracted-item">
                        <div class="label">Płeć</div>
                        <div class="val">Mężczyzna</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- KROK 3 -->
        <div class="section-card">
            <h2>3. Obliczenia modelu ML i przewidywany czas</h2>
            <p>Wytrenowany model uczenia maszynowego (ML) przekształca wyciągnięte parametry na przewidywany wynik półmaratonu oraz oblicza wymagane tempo na dystansie.</p>
            
            <div class="ui-mockup">
                <div class="result-panel">
                    <div class="result-header">
                        ⏱️ Przewidywany czas półmaratonu: 01:49:02
                    </div>
                    <div class="result-sub">
                        Średnie wymagane tempo: <strong>5:10 min/km</strong>
                    </div>
                </div>
            </div>
        </div>

    </div>

</body>
</html>
