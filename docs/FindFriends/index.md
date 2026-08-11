# Find Friends

Aplikacja służy do inteligentnego grupowania uczestników na podstawie ich odpowiedzi w ankiecie powitalnej. Wykorzystuje model klasteryzacji zbudowany w PyCaret, który analizuje cechy użytkowników i przypisuje ich do jednej z wcześniej wytrenowanych grup o podobnych preferencjach i charakterystykach.

Po uruchomieniu aplikacji użytkownik wypełnia krótki formularz w panelu bocznym, podając: wiek, poziom wykształcenia, ulubione zwierzęta, preferowane miejsca, płeć.

Na podstawie tych danych aplikacja:

- Wczytuje wytrenowany model klasteryzacji oraz pełny zbiór uczestników.
- Przewiduje, do którego klastra (grupy) należy użytkownik.
- Wyświetla nazwę i opis tej grupy, pobrany z pliku JSON zawierającego charakterystyki klastrów.
- Pokazuje liczbę osób podobnych do użytkownika, czyli tych, którzy trafili do tego samego klastra.
- Prezentuje wizualizacje danych dotyczące tej grupy, m.in.: rozkład wieku, poziom wykształcenia, ulubione zwierzęta, preferowane miejsca, płeć.

Wszystkie wykresy generowane są za pomocą Plotly, co zapewnia przejrzystą i interaktywną prezentację danych.

Dzięki temu użytkownik może szybko zobaczyć, do jakiej grupy osób jest najbardziej podobny oraz poznać jej profil. Aplikacja pomaga w budowaniu społeczności, ułatwiając znajdowanie osób o zbliżonych zainteresowaniach i cechach.

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