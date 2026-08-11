# LinguaPulse

LinguaPulse to interaktywna aplikacja do nauki języków obcych, która łączy tłumaczenie, korektę językową, analizę gramatyczną, generowanie profesjonalnych wiadomości oraz syntezę mowy w jednym spójnym narzędziu. Projekt wykorzystuje multimodalne podejście, integrując tekst, analizę językową i audio, aby maksymalnie wspierać proces uczenia się.

Aplikacja oferuje cztery główne funkcje pracy z językiem:

-   Tłumaczenie — profesjonalne przekłady z polskiego na wybrany język, z zachowaniem naturalnego stylu i kontekstu.

-   Korekta językowa — analiza błędów, poprawiona wersja tekstu, wyjaśnienia po polsku oraz przykłady użycia.

-   Profesjonalne wiadomości — automatyczne redagowanie tekstów w wybranym stylu (formalnym, biznesowym, przyjaznym itd.).

-   Wyjaśnienie słów i gramatyki — szczegółowa analiza tekstu, tłumaczenie, omówienie słownictwa i konstrukcji gramatycznych oraz wskazówki do nauki.

LinguaPulse umożliwia również:

-   Generowanie nagrań audio w różnych głosach (np. narracyjny, neutralny, głęboki), co wspiera rozwój wymowy i rozumienia ze słuchu.

-   Zarządzanie historią pracy — filtrowanie, wyszukiwanie, oznaczanie ulubionych wyników, ponowne użycie treści oraz eksport danych do pliku CSV.

-   Bezpieczne logowanie użytkowników oraz przechowywanie historii w lokalnej bazie SQLite.

Dzięki połączeniu sztucznej inteligencji, analizy językowej i funkcji audio, LinguaPulse tworzy środowisko, które sprawia, że nauka języków jest bardziej efektywna, intuicyjna i angażująca.

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