from django.urls import path
from . import views

urlpatterns = [
    path('payment/<int:booking_id>/', views.payment_view, name='payment_view'),
    path('payment_success/', views.payment_success, name='payment_success'),
]
