




function openDrawer(){

    document.getElementById('myDrawer').classList.toggle('active')
}

function closeDrawer(){
    document.getElementById('myDrawer').classList.toggle('active')
}



// Define an array to store cart items
let cartItems = [];

// Function to add items to the cart
function addToCart(productName, price, itemCount) {
    const newItem = {
        name: productName,
        price: price,
        count: itemCount
    };

    cartItems.push(newItem);

    updateCartDisplay();
}

function updateCartDisplay() {
    const cartList = document.querySelector('.cart-list');

    cartList.innerHTML = '';

    cartItems.forEach((item, index) => {
        const listItem = document.createElement('li');

        const itemInfo = document.createElement('span');
        itemInfo.textContent = `${item.name} - $${item.price.toFixed(2)} - ${item.count}`;

        const itemRemove = document.createElement('button');
        itemRemove.textContent = 'Remove';
        itemRemove.onclick = () => removeFromCart(index);
        itemRemove.classList.add('rmvbtn');

        listItem.appendChild(itemInfo);
        listItem.appendChild(itemRemove);

        cartList.appendChild(listItem);
    });
}

function removeFromCart(index) {
    cartItems.splice(index, 1);

    updateCartDisplay();
}

