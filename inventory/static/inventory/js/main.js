




function openDrawer(){

    document.getElementById('myDrawer').classList.toggle('active')
}

function closeDrawer(){
    document.getElementById('myDrawer').classList.toggle('active')
}



let cart_item = [];

function addToCart(productName, price, image) {
    const item ={
        name:productName,
        price:price,
        image:image
    };
    
    cart_item.push(item)

    updateCartDisplay();
}

function updateCartDisplay() {
    
}