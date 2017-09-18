from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from .models import BathBombs, Order, Invoice, Testimonial
from .cart_service import CartService

def index(request):
    bath_bombs = BathBombs.objects.all()
    testimonials = Testimonial.objects.all()
    return render(request, 'home.html', {'bath_bombs': bath_bombs, 'testimonials': testimonials})


def create_invoice(request):
    total_price = 0
    invoice = Invoice()
    invoice.contact_name = request.user_name
    invoice.contact_email = request.user_email

    for order in request.orders:
        total_price += order.get_price()
    invoice.total_price = total_price
    invoice.save()


def create_order(request):
    if request.is_ajax():
        bath_bomb_id = request.POST.get('bathbomb_id')
        bath_bomb = BathBombs.objects.get(pk=bath_bomb_id)
        order = Order(
            bath_bomb = bath_bomb,
            quantity = request.POST.get('quantity')
        )
        order.save()

        cart_service = CartService()
        cart = cart_service.create_or_update(request, order.pk)
        response = JsonResponse({'success': True})
        response.set_cookie('cart', cart)
        return response
    else:
        return False

def remove_item_from_cart(request):
    if request.is_ajax:
        order_id = request.POST.get('order_id')
        Order.objects.filter(id=order_id).delete()

        cart_service = CartService()
        cart = cart_service.remove_order_from_cart(request, order_id)
        response = JsonResponse({'success': True})
        response.set_cookie('cart', cart)
        return response


def get_cart_item_count(request):
    if request.is_ajax():
        cart_service = CartService()
        item_count = cart_service.get_cart_item_count(request)
        response = JsonResponse({'item_count': item_count})
        return response
    else:
        return False

def get_shopping_cart(request):
    cart_service = CartService()
    orders_in_cart = cart_service.get_orders_in_cart(request)
    orders = Order.objects.filter(id__in=orders_in_cart)
    total_price = 0
    for order in orders:
        total_price += order.get_price()

    return render(request, 'shopping-cart.html', {'orders': orders, 'total_price' : total_price})


def update_order(request):
    if request.is_ajax():
        order = Order.objects.get(id=request.POST.get("order_id"))
        order.quantity = request.POST.get('quantity')
        order.save()
        response = JsonResponse({'quantity' : order.quantity, 'price' : order.bath_bomb.price})
        return response

def create_testimonial(request):
    if request.is_ajax():
        if Testimonial.objects.filter(user=request.user).exists():
            response = JsonResponse({'message' : 'We have already received your feedback, thank you!'})
            return response
        else:
            testimonial = Testimonial(
                user = request.user,
                feedback = request.POST.get("feedback")
            )
            testimonial.save()
            response = JsonResponse({'message': 'Thank you'})
            return response
    else:
        return redirect('/')


def thank_you(request):
   return render(request, 'testimonial_thankyou.html')
