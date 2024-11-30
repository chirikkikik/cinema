from django.urls import path
from . import views

urlpatterns = [
    #path('booking/', views.add_ticket_to_booking, name='booking'),
    path('choose_screening/', views.choose_screening, name='choose_screening'),
    path('choose_seat/', views.choose_seat, name='choose_seat'),
    path('booking_summary/<int:booking_id>/<int:screening_id>/', views.booking_summary, name='booking_summary'),
]
