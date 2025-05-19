document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    form.addEventListener("submit", function() {
        const submitButton = form.querySelector("input[type='submit']");
        submitButton.disabled = true;
        submitButton.value = "Logging in...";
    });
});
