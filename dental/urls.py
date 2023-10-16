from django.contrib import admin
from django.urls import path

from .views import contact_view, success_view


urlpatterns = [
    path('email/', contact_view, name='email'),
    path('success/', success_view, name='success'),
   
]
