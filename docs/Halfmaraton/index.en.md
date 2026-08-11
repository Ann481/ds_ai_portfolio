# **Half Marathon Time Calculator**

An application that estimates half marathon completion time based on runner data. Trained on dataset from the Wrocław Half Marathon 2023 and 2024 (~18,000 results).

The user inputs their gender, age, and 5 km pace. The app uses OpenAI to extract data from the text and then predicts the finish time.

<a href="app.py" class="md-button md-button--primary">Pobierz Notebook</a>

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