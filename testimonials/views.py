from django.shortcuts import render
from django.contrib.auth.mixins import redirect_to_login, LoginRequiredMixin
from django.views import generic
from . import models
# Create your views here.

class CreateTestimonial(generic.TemplateView):
    template_name = "create_form.html"