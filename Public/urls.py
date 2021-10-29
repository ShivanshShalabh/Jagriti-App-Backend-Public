from django.urls import path
from django.urls.conf import include
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('base', views.base, name="Base"),
    path('about', views.about, name="About"),
    path('jagrukta zone', views.jagrukta, name="Jagrukta Zone"),
    path('volunteer', views.volunteer, name="Volunteer With Us"),
]
