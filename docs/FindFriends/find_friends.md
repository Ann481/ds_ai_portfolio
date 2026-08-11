<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Find Friends – Opis Projektu</title>
    <style>
        :root {
            --bg-color: #ffffff;
            --text-color: #000000;
            --text-muted: #4b5563;
            --card-bg: #f9fafb;
            --border-color: #e5e7eb;
            --accent-color: #2563eb;
            --font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-color);
            font-family: var(--font-family);
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
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 20px;
        }

        h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
            color: var(--text-color);
        }

        .subtitle {
            font-size: 1.2rem;
            color: var(--text-muted);
        }

        .section {
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 24px;
            margin-bottom: 30px;
        }

        h2 {
            font-size: 1.5rem;
            margin-bottom: 16px;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 8px;
            color: var(--text-color);
        }

        p {
            margin-bottom: 12px;
            color: var(--text-color);
        }

        ul {
            margin-left: 20px;
            margin-bottom: 16px;
        }

        li {
            margin-bottom: 6px;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 16px;
            margin-top: 16px;
        }

        .card {
            background-color: #ffffff;
            border: 1px solid var(--border-color);
            border-radius: 6px;
            padding: 16px;
        }

        .card h3 {
            font-size: 1.1rem;
            margin-bottom: 8px;
            color: var(--text-color);
        }

        .card p {
            font-size: 0.95rem;
            color: var(--text-muted);
            margin-bottom: 0;
        }

        footer {
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid var(--border-color);
            color: var(--text-muted);
            font-size: 0.9rem;
        }
    </style>
</head>
<body>

    <div class="container">

        <header>
            <h1>🤝 Find Friends</h1>
            <p class="subtitle">Aplikacja do znajdowania osób o podobnych zainteresowaniach</p>
        </header>

        <!-- OPIS PROJEKTU -->
        <div class="section">
            <h2>📌 O projekcie</h2>
            <p>
                <strong>Find Friends</strong> to aplikacja stworzona z myślą o uczestnikach kursu, której głównym celem jest łączenie ludzi i pomaganie im w znajdowaniu osób o zbliżonych profilach i pasjach.
            </p>

        </div>

        <!-- JAK TO DZIAŁA -->
        <div class="section">
            <h2>⚙️ Jak to działa?</h2>
            <p>Proces przydzielania do grupy i analizy składa się z kilku kroków:</p>
            <ul>
                <li><strong>Wprowadzenie danych:</strong> Użytkownik podaje podstawowe informacje o sobie, takie jak: wiek, wykształcenie, ulubione zwierzęta, preferowane miejsce spędzania czasu oraz płeć.</li>
                <li><strong>Klasteryzacja:</strong> Algorytm grupowania (klasteryzacji) analizuje wprowadzone dane i przypisuje użytkownika do klastra osób o najbardziej zbliżonym profilu.</li>
                <li><strong>Generowanie opisu (LLM):</strong> Opis i charakterystyka każdej wyodrębnionej grupy są automatycznie tworzone przez duży model językowy (LLM).</li>
                <li><strong>Wizualizacja danych:</strong> Dla każdej grupy generowane są interaktywne wykresy prezentujące rozkład cech jej członków (np. rozkład wieku, płci czy ulubionych zwierząt).</li>
            </ul>
        </div>

        <!-- KLUCZOWE FUNKCJONALNOŚCI -->
        <div class="section">
            <h2>🚀 Funkcjonalności interfejsu</h2>
            <div class="grid">
                <div class="card">
                    <h3>📝 Formularz profilowy</h3>
                    <p>Wygodny panel boczny pozwalający na określenie swoich preferencji i cech.</p>
                </div>
                <div class="card">
                    <h3>🤖 Automatyczny opis grupy</h3>
                    <p>Unikalny podsumowujący opis profilu generowany przez AI dla każdego klastra.</p>
                </div>
                <div class="card">
                    <h3>📊 Wykresy i Statystyki</h3>
                    <p>Wizualna analiza rozkładu wieku, płci oraz upodobań wśród przypisanych znajomych.</p>
                </div>
            </div>
        </div>



    </div>

</body>
</html>