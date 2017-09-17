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
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='blog'),
    url(r'^(?P<post_id>\d+)$', views.get_blog, name='get_post'),
    url(r'like$', views.like_post, name='like_post'),
    url(r'comment$', views.comment),
    url(r'comment/edit/(?P<comment_id>\d+)$', views.edit_comment, name='edit_comment'),
    url(r'comment/delete$', views.delete_comment, name='delete_comment'),
]
