"""afteralongday URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^add-to-cart$', views.create_order),
    url(r'^remove-from-cart$', views.remove_item_from_cart),
    url(r'^update-order-quantity$', views.update_order),
    url(r'^cart-item-count$', views.get_cart_item_count),
    url(r'^shopping-cart$', views.get_shopping_cart, name='shopping-cart'),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
    url(r'^testimonial/', views.create_testimonial),
    url(r'^accounts/', include('accounts.urls'))
]
