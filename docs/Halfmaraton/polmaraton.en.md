<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Half Marathon Time Estimator – How It Works</title>
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
            <h1>🏃 Half Marathon Time Estimator</h1>
            <p>ML + OpenAI application based on natural language data input</p>
        </header>

        <!-- STEP 1 -->
        <div class="section-card">
            <h2>1. Natural language data entry</h2>
            <p>Users don't need to fill out forms or dropdown lists. Simply type a brief sentence about yourself into a single text field.</p>
            
            <div class="ui-mockup">
                <div class="ui-label">Introduce yourself and enter your details:</div>
                <div class="ui-hint">Type a brief introduction in the box below, e.g.: <i>Hi, my name is Tom, I'm 30 years old, and my 5K personal best is 23 minutes 15 seconds.</i></div>
                <div class="ui-textarea" style="color: #6b7280;">Enter your text here...</div>
                <div class="ui-button">Estimate Half Marathon Time</div>
            </div>
        </div>

        <!-- STEP 2 -->
        <div class="section-card">
            <h2>2. Parameter extraction via OpenAI</h2>
            <p>The OpenAI model (LLM) analyzes natural text and automatically extracts key data: <strong>name, age, 5K time (pace), and gender</strong>.</p>
            
            <div class="ui-mockup">
                <div class="ui-label">Introduce yourself and enter your details:</div>
                <div class="ui-textarea">Hi, my name is Adrian, I'm 35 years old, and my 5K personal best is 25 minutes.</div>
                <div class="ui-button">Estimate Half Marathon Time</div>

                <div class="ui-greeting">Hi Adrian!</div>

                <div class="extracted-grid">
                    <div class="extracted-item">
                        <div class="label">Age</div>
                        <div class="val">35 y/o</div>
                    </div>
                    <div class="extracted-item">
                        <div class="label">5K Time</div>
                        <div class="val">25.00 min</div>
                    </div>
                    <div class="extracted-item">
                        <div class="label">Gender</div>
                        <div class="val">Male</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- STEP 3 -->
        <div class="section-card">
            <h2>3. ML Model calculation and predicted time</h2>
            <p>The trained machine learning (ML) model converts extracted parameters into a predicted half marathon result and calculates the required average pace.</p>
            
            <div class="ui-mockup">
                <div class="result-panel">
                    <div class="result-header">
                        ⏱️ Predicted half marathon time: 01:49:02
                    </div>
                    <div class="result-sub">
                        Average required pace: <strong>5:10 min/km</strong>
                    </div>
                </div>
            </div>
        </div>

    </div>

</body>
</html>