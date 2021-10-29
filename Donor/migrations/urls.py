from django.urls import path
from django.urls.conf import include
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('donate', views.donate, name="Donate Now"),
]
