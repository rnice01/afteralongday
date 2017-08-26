from lib.helpers import CookieHelper
from django.http import HttpResponse, JsonResponse

class CartService:
    cookie_helper = None
    cart_cookie = "cart"

    def __init__(self):
        self.cookie_helper = CookieHelper()

    def create_or_update(self, request, value):
        current_cart = request.COOKIES.get('cart', '')
        updated_cart = self.cookie_helper.add(current_cart, value)
        response = JsonResponse({'success': True})
        response.set_cookie('cart', updated_cart)
        return response

    def get_cart_item_count(self, request):
        current_cart = request.COOKIES.get('cart', '')
        cart_list = self.cookie_helper.to_list(current_cart)
        item_count = len(cart_list)
        response = JsonResponse({'item_count' : item_count})
        return response