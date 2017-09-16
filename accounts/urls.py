from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^login/$', login, {'template_name' : 'accounts/login.html'}),
    url(r'^logout/$', logout, {'next_page' : '/'}),
    url(r'^register/$', views.register),
]