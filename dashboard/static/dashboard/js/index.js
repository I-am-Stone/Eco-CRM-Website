document.addEventListener('DOMContentLoaded', function() {
    const visibilityCheckbox = document.getElementById('visibility-checkbox');
    
    // Set initial value
    if (visibilityCheckbox) {
        visibilityCheckbox.value = visibilityCheckbox.checked ? 'true' : 'false';
        console.log('Initial visibility value:', visibilityCheckbox.value);
        
        visibilityCheckbox.addEventListener('change', function() {
            this.value = this.checked ? 'true' : 'false';
            console.log('Visibility value:', this.value);
        });
    } else {
        console.log('Checkbox not found - check your HTML ID');
    }
});