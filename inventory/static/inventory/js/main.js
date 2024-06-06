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
  const csrftoken = getCookie('csrftoken');

  fetch("{% url 'home' %}", {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken,
      },
      body: JSON.stringify({
          'remove_item_id': productId
      })
  })
  .then(response => response.json())
  .then(data => {
      if (data.message) {
          location.reload();  // Refresh the page to update the cart
      } else {
          alert(data.error);
      }
  });
}
