// static/js/script.js

// Form validation (Basic)
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function(event) {
        let isValid = true;

        form.querySelectorAll('input, textarea').forEach(input => {
            if (input.required && input.value.trim() === '') {
                isValid = false;
                alert(input.name + " is required!");
            }
        });

        if (!isValid) {
            event.preventDefault();
        }
    });
});

// Confirm before deletion
function confirmDeletion(eventId) {
    if (!confirm("Are you sure you want to delete this event?")) {
        event.preventDefault();
    }
}
