# Find Friends

The application is designed to intelligently group participants based on their answers in a welcome survey. It uses a clustering model built with PyCaret, which analyzes user characteristics and assigns them to one of several pre‑trained groups with similar preferences and traits.

After launching the application, the user fills out a short form in the sidebar, providing: age education level, favorite animals, preferred places, gender.

Based on this information, the application:

- Loads the trained clustering model and the full dataset of participants.
- Predicts which cluster (group) the user belongs to.
- Displays the name and description of that group, retrieved from a JSON file containing cluster characteristics.
- Shows how many people are similar to the user, meaning those who fall into the same cluster.
- Presents data visualizations for that group, including: age distribution, education level favorite animals, preferred places, gender.

All charts are generated using Plotly, ensuring clear and interactive data presentation.

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