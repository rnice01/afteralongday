from lib.helpers import CookieHelper

class CartService:
    cookie_helper = None
    cart_cookie = "cart"

    def __init__(self):
        self.cookie_helper = CookieHelper()

    def get_cart_cookie(self, request):
        return request.COOKIES.get(self.cart_cookie, '')


    def create_or_update(self, request, value):
        current_cart = self.get_cart_cookie(request)
        updated_cart = self.cookie_helper.add(current_cart, value)
        return updated_cart


    def get_cart_item_count(self, request):
        current_cart = self.get_cart_cookie(request)
        cart_list = self.cookie_helper.to_list(current_cart)
        item_count = len(cart_list)
        return item_count


    def get_orders_in_cart(self, request):
        current_cart = self.get_cart_cookie(request)
        orders_in_cart = self.cookie_helper.to_list(current_cart)
        return orders_in_cart

    def remove_order_from_cart(self, request, order_id_to_remove):
        current_cart = self.get_cart_cookie(request)
        cart = self.cookie_helper.remove(current_cart, order_id_to_remove)
        return cart
