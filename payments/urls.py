from . import views
from django.urls import path

urlpatterns = [
    path('pay/<int:booking_id>/', views.payment_view, name='payment_view'),
    path('success/', views.payment_success, name='payment_success'),
]
