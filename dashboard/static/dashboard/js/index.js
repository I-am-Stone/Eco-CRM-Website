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


document.addEventListener('DOMContentLoaded', function(){
    const product_action = document.getElementById('action');
    console.log(product_action.value);

    if (product_action){
        console.log("initial Value:",product_action)
        product_action.addEventListener('change', function () {
            console.log('Updated value:', product_action.value);
            const SelectedValue = this.value
            console.log(SelectedValue)
            if (SelectedValue) {
                window.location.href = SelectedValue;
            }else{
                console.log('no valid option')
            }
        });

    }else {
        console.log('Select element not found - check your HTML ID');
    }

});