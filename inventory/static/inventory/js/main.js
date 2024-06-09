function openDrawer() {
  document.getElementById("myDrawer").classList.toggle("active");
}

function closeDrawer() {
  document.getElementById("myDrawer").classList.toggle("active");
}

// main.js
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

function removeFromCart(productId) {
    fetch("{% url 'home' %}", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}'  // Include CSRF token for security
        },
        body: JSON.stringify({ 'product_id': productId })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Item removed from cart');
            // Optionally, you can remove the item from the DOM here
            document.querySelector(`#item-${productId}`).remove();
        } else {
            alert('Error: ' + data.message);
        }
    })
    .catch(error => console.error('Error:', error));
}
