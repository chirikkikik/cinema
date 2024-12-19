from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('payment_form/<int:booking_id>/', views.payment_form, name='payment_form'),
    path('payment_success/', views.payment_success, name='payment_success'),
]
