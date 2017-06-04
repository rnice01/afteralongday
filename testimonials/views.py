from django.shortcuts import render
from django.views import generic
from .forms import CreateTestimonialForm
# Create your views here.

def thank_you(request):
   return render(request, 'testimonial_thankyou.html')


class CreateTestimonialView(generic.CreateView):
   form_class = CreateTestimonialForm
   template_name = 'testimonial_form.html'
   success_url = '/testimonial/thank-you/'
