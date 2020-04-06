from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.registration_view,name='register'),
    path('user_details/',views.user_details,name="user")
]