// static/script.js
document.addEventListener('DOMContentLoaded', function () {
    // Get all the anchor tags (EV makes)
    const makeLinks = document.querySelectorAll('a');

    // Add click event listeners to the make links
    makeLinks.forEach(function (makeLink) {
        makeLink.addEventListener('click', function (event) {
            // Prevent the default behavior of anchor tags
            event.preventDefault();

            // Get the href attribute of the clicked link
            const href = makeLink.getAttribute('href');

            // Make an AJAX request to the server to load the make details
            fetch(href)
                .then(function (response) {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.text();
                })
                .then(function (data) {
                    // Replace the content of the page with the loaded data
                    document.body.innerHTML = data;
                })
                .catch(function (error) {
                    console.error('There was a problem with the fetch operation:', error);
                });
        });
    });
});
