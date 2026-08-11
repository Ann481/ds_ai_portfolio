<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LinguaPulse – Language Helper | Project Description</title>
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
            <p>Language Helper – a comprehensive tool for foreign language learning, translation, grammar analysis, and audio pronunciation generation.</p>
        </header>

        <!-- MAIN DESCRIPTION -->
        <div class="section-card">
            <h2>📌 About the Project</h2>
            <p>
                <strong>LinguaPulse</strong> is a versatile language assistant designed for effective and enjoyable foreign language learning.
                The application goes beyond standard word and sentence translation – it analyzes context, corrects errors, adjusts communication style, and provides detailed explanations of grammatical intricacies alongside vocabulary and learning tips.
            </p>

            <div class="features-grid">
                <div class="feature-card">
                    <h3>🌐 Translation</h3>
                    <p>Fast and accurate translation of text into selected foreign languages.</p>
                </div>
                <div class="feature-card">
                    <h3>📝 Language Proofreading</h3>
                    <p>Detection and correction of spelling, punctuation, and grammar mistakes.</p>
                </div>
                <div class="feature-card">
                    <h3>✨ Polished Version</h3>
                    <p>Enhancing tone and natural flow of expression for a better sound.</p>
                </div>
                <div class="feature-card">
                    <h3>📚 Vocabulary & Grammar Explanation</h3>
                    <p>Deconstruction of sentences, vocabulary breakdown, and grammar rule explanations.</p>
                </div>
            </div>
        </div>

        <!-- EXAMPLE 1: TRANSLATION & PRONUNCIATION GENERATOR -->
        <div class="section-card">
            <h2>1. Mode: Translation + Audio Pronunciation Generator</h2>
            <p>The user selects the translation feature, target language, and voice actor, then enters text in English. Once the result is generated, a text-to-speech (TTS) module is also available.</p>

            <div class="app-mockup">
                <div style="font-weight: 600; margin-bottom: 12px;">Select feature:</div>
                <div class="radio-group">
                    <div class="radio-option active"><span class="radio-dot"></span> 🌐 Translation</div>
                    <div class="radio-option"><span class="radio-dot"></span> 📝 Language Proofreading</div>
                    <div class="radio-option"><span class="radio-dot"></span> ✨ Polished Message</div>
                    <div class="radio-option"><span class="radio-dot"></span> 📚 Vocabulary & Grammar Explanation</div>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label>🌏 Select language:</label>
                        <div class="select-box">ES Spanish</div>
                    </div>
                    <div class="form-group">
                        <label>🔊 Select voice:</label>
                        <div class="select-box">Nova - female</div>
                    </div>
                </div>

                <div class="form-group">
                    <label>Enter text in English:</label>
                    <div class="textarea-box">How do I get from the airport to the center of Barcelona?</div>
                </div>

                <div class="btn-submit">🚀 Submit</div>

                <div style="margin-top: 20px;">
                    <div class="status-badge">Done! (2.54s)</div>
                    <div class="result-box">
                        <h3>Result:</h3>
                        <p style="font-size: 1.1rem; color: #111827; margin-bottom: 15px;">¿Cómo llego del aeropuerto al centro de Barcelona?</p>
                        
                        <div style="border-top: 1px solid var(--card-border); padding-top: 15px; margin-top: 15px;">
                            <h3 style="display: flex; align-items: center; gap: 8px;">🔊 Pronunciation Generator</h3>
                            <label style="font-size: 0.85rem; color: var(--text-muted); display: block; margin: 8px 0 4px 0;">Text for audio:</label>
                            <div class="textarea-box" style="height: 50px; margin-bottom: 10px;">¿Cómo llego del aeropuerto al centro de Barcelona?</div>
                            <div class="btn-submit">🎧 Generate Audio</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- EXAMPLE 2: VOCABULARY & GRAMMAR EXPLANATION -->
        <div class="section-card">
            <h2>2. Mode: Vocabulary & Grammar Explanation</h2>
            <p>The application generates a structured educational report containing natural translation, key vocabulary with definitions, grammar rules, and practical study tips.</p>

            <div class="app-mockup">
                <div style="font-weight: 600; margin-bottom: 12px;">Select feature:</div>
                <div class="radio-group">
                    <div class="radio-option"><span class="radio-dot"></span> 🌐 Translation</div>
                    <div class="radio-option"><span class="radio-dot"></span> 📝 Language Proofreading</div>
                    <div class="radio-option"><span class="radio-dot"></span> ✨ Polished Message</div>
                    <div class="radio-option active"><span class="radio-dot"></span> 📚 Vocabulary & Grammar Explanation</div>
                </div>

                <div class="result-box">
                    <h3>Result:</h3>
                    <ol class="explanation-list">
                        <li><strong>Natural translation:</strong> "How do I get from the airport to the center of Barcelona?"</li>
                        <li><strong>Key words & phrases:</strong>
                            <ul>
                                <li><strong>aeropuerto</strong> - airport</li>
                                <li><strong>centro</strong> - center</li>
                                <li><strong>llego</strong> - I arrive, I get to (form of the verb "llegar")</li>
                                <li><strong>cómo</strong> - how</li>
                                <li><strong>del</strong> - from the (contraction of "de" and "el")</li>
                            </ul>
                        </li>
                        <li><strong>Grammar breakdown:</strong>
                            <ul>
                                <li>The verb "llegar" is a regular verb in Spanish, meaning its present tense conjugation follows standard rules. In the first person singular (yo), it takes the form "llego".</li>
                                <li>The use of "del" (de + el) is standard in Spanish, where "de" means "from" and "el" is the masculine article "the". In the context of the question, it indicates traveling from a specific location (the airport) to another (the center).</li>
                            </ul>
                        </li>
                        <li><strong>Study tips:</strong>
                            <ul>
                                <li>Practice using the question word "¿Cómo...?" in various contexts to become more comfortable asking questions.</li>
                                <li>Learn travel-related vocabulary to communicate smoothly in transportation scenarios.</li>
                                <li>Practice regular verb conjugations to understand how they function across different tenses and subjects.</li>
                                <li>Try creating your own sentences using these new words and phrases to reinforce your learning.</li>
                            </ul>
                        </li>
                    </ol>
                </div>
            </div>
        </div>

        <footer>
            <p style="text-align: center; color: var(--text-muted); font-size: 0.85rem; margin-top: 30px; border-top: 1px solid var(--card-border); padding-top: 20px;">
                LinguaPulse Project • AI-Powered Language Helper
            </p>
        </footer>

    </div>

</body>
</html>