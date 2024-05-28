function openDrawer() {
  document.getElementById("myDrawer").classList.toggle("active");
}

function closeDrawer() {
  document.getElementById("myDrawer").classList.toggle("active");
}

// main.js
console.log("main.js is loaded");

$(document).ready(function () {
  $(".remove-item-btn").click(function () {
    console.log("Remove button clicked"); // Add this line for debugging
    var itemId = $(this).data("item-id");
    $.ajax({
      type: "POST",
      url: "/remove-from-cart/",
      data: {
        remove_item_id: itemId,
        csrfmiddlewaretoken: "{{ csrf_token }}",
      },
      success: function (data) {
        // Update the cart display as needed
        location.reload(); // Refresh the page for simplicity, you can update the cart dynamically instead
      },
    });
  });
});
