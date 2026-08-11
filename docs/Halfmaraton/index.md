# Kalkulator czasu półmaratonu

Aplikacja szacująca czas ukończenia półmaratonu na podstawie danych biegacza. Wytrenowana na danych z Półmaratonu Wrocławskiego 2023 i 2024 (~18 000 wyników).

Użytkownik podaje płeć, wiek i tempo na 5 km. Aplikacja używa OpenAI do wyłuskania danych z tekstu, a następnie przewiduje czas ukończenia.

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