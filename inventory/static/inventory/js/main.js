




function openDrawer(){

    document.getElementById('myDrawer').classList.toggle('active')
}

function closeDrawer(){
    document.getElementById('myDrawer').classList.toggle('active')
}



let cart_item = [];

function addToCart(productName, price, ImageURL) {
    const item = {
        name: productName,
        price: price,
        image:ImageURL
    };
    
    cart_item.push(item);

    updateCartDisplay();
}

function updateCartDisplay() {
    const cartList = document.querySelector('.cart-list');

    cartList.innerHTML = '';

    cart_item.forEach((item, index) => {
        const listItem = document.createElement('li');

        const img = document.createElement('img');
        img.src = item.image
        img.alt = item.name
        img.width = '40px'

        const itemInfo = document.createElement('span');

        itemInfo.textContent = `${item.name} - $${item.price.toFixed(2)}`;

        const itemremove = document.createElement('button');
        itemremove.textContent = 'Remove';
        itemremove.onclick = () => removeFromCart(index);
        itemremove.classList.add('rmvbtn')

        listItem.appendChild(img)
        listItem.appendChild(itemInfo)
        listItem.appendChild(itemremove)


        cartList.appendChild(listItem);
    });
}

function removeFromCart(index) {
    cart_item.splice(index, 1);
    updateCartDisplay();
}

