from views import get_cart_items
def cart_context(request):
    cart = request.session.get('cart',{})
    cart_items, total_price = get_cart_items(cart)
    return {
        'cart_items': cart_items,
        'total_price': total_price
    }