from inventory.models import *


class CartService:
    @classmethod
    def get_cart_items(cls,cart_dict):
        if not cart_dict:
            return [], 0

        cart_items = []
        total_price = 0
        product_ids = cart_dict.keys()
        products = ProductInventory.objects.prefetch_related("media_product_inventory").filter(pk__in=product_ids)

        for product in products:
            quantity = cart_dict[str(product.pk)]
            item_total = product.retail_price * quantity
            product_name = product.product.name
            media_info = [{'url': media.image, 'alt_text': media.alt_text}
                        for media in product.media_product_inventory.all()]
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'item_total': item_total,
                'product_name': product_name,
                'media_info': media_info,
                'retail_price': product.retail_price,
            })
            total_price += item_total
        return cart_items, total_price

    @classmethod
    def add_product_to_carts(cls, request):  
        cart = request.session.get('cart', {})
        if request.method == "POST" and 'product_id' in request.POST:
            product_id = request.POST.get('product_id')
            quantity = int(request.POST.get('quantity', 1))
            if product_id in cart:
                cart[product_id] += quantity
            else:
                cart[product_id] = quantity
            request.session['cart'] = cart
        
        cart_items, total_price = cls.get_cart_items(cart)  

        return {
            'cart_items': cart_items,
            'total_price': total_price

        }
    
    @classmethod
    def remove_from_cart(cls, request):
        cart = request.session.get('cart', {})
        if request.method == "POST":
            remove_item_id = request.POST.get('remove_item_id')
            if remove_item_id in cart:
                del cart[remove_item_id]
                request.session['cart'] = cart
        
        cart_items, total_price = cls.get_cart_items(cart)
        return {
            'cart_items': cart_items,
            'total_price': total_price
        }


