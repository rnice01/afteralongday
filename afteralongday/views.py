from django.shortcuts import render
from .models import BathBombs
from testimonials.models import Testimonial

def index(request):
    bath_bombs = BathBombs.objects.all()
    testimonials = Testimonial.objects.order_by('id')[:3]
    return render(request, 'home.html', {'bath_bombs': bath_bombs, 'testimonials': testimonials})