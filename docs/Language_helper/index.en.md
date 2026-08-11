# LinguaPulse

LinguaPulse is an interactive language‑learning application that combines translation, language correction, grammar analysis, professional message generation, and speech synthesis into one cohesive tool. The project uses a multimodal approach, integrating text, linguistic analysis, and audio to effectively support the learning process.

The application offers four core language‑processing features:

-   Translation — professional translations from Polish into the selected language, preserving natural style and context.

-   Language correction — error analysis, an improved version of the text, explanations in Polish, and usage examples.

-   Professional messages — automatic editing of texts in a chosen style (formal, business, friendly, casual, etc.).

-   Word and grammar explanation — detailed text analysis, translation, vocabulary breakdown, grammar explanations, and learning tips.

LinguaPulse also enables:

-   Audio generation in multiple voices (e.g., narrative, neutral, deep), supporting pronunciation practice and listening comprehension.

-   Work history management — filtering, searching, marking favorites, reusing content, and exporting data to CSV.

-   Secure user authentication and local storage of history in a SQLite database.

By combining artificial intelligence, linguistic analysis, and audio features, LinguaPulse creates an environment that makes language learning more effective, intuitive, and engaging.

<a href="app_LinguaPulse.py" class="md-button md-button--primary">Pobierz Notebook</a>

<script>
function resizeIframeToFitContent(iframe) {
    iframe.style.height = (iframe.contentWindow.document.documentElement.scrollHeight + 50) + "px";
    iframe.contentDocument.body.style["overflow"] = 'hidden';
}
window.addEventListener('load', function() {
    var iframe = document.getElementById('content');
    resizeIframeToFitContent(iframe);
});
window.addEventListener('resize', function() {
    var iframe = document.getElementById('content');
    resizeIframeToFitContent(iframe);
});
</script>