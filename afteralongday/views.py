from django.http import JsonResponse
from django.shortcuts import render
from .models import BathBombs, Order, Invoice
from testimonials.models import Testimonial

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
        order = Order()
        bath_bomb = BathBombs.objects.get(pk=request.POST.get('bathbomb_id'))
        order.bath_bomb = request.POST.get('bathbom_id')
        order.quantity = request.POST.get('quantity')
        order.save()
        return JsonResponse({'order_id' : order.pk})
    else:
        return False