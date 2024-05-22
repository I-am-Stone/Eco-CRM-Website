




function openDrawer(){

    document.getElementById('myDrawer').classList.toggle('active')
}

function closeDrawer(){
    document.getElementById('myDrawer').classList.toggle('active')
}


// let cartItems = []; 

// function addToCart(productName, price, itemCount) {
//     const newItem = {
//         name: productName,
//         price: price,
//         count: parseInt(itemCount) 
//     };

//     cartItems.push(newItem);

//     updateCartDisplay();
// }


// function updateCartDisplay() {
//     const cartList = document.querySelector('.cart-list');
//     cartList.innerHTML = ''; 

//     cartItems.forEach((item, index) => {
//         const listItem = document.createElement('li');
//         const itemInfo = document.createElement('span');
//         itemInfo.textContent = `${item.name} - Rs.${item.price.toFixed(2)} - Quantity: ${item.count}`;

//         const itemRemove = document.createElement('button');
//         itemRemove.textContent = 'Remove';
//         itemRemove.onclick = () => removeFromCart(index);
//         itemRemove.classList.add('rmvbtn');

//         listItem.appendChild(itemInfo);
//         listItem.appendChild(itemRemove);
//         cartList.appendChild(listItem);
//     });
// }

// function removeFromCart(index) {
//     cartItems.splice(index, 1); 
//     updateCartDisplay();
// }

