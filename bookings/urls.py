from django.urls import path
from . import views

urlpatterns = [
    path('choose_screening/<int:movie_id>/', views.choose_screening, name='choose_screening'),
    path('choose_seat/<int:screening_id>/', views.choose_seat, name='choose_seat'),
    path('booking_summary/<int:booking_id>/', views.booking_summary, name='booking_summary'),
    path('remove_ticket_from_booking/<int:ticket_id>/', views.remove_ticket_from_booking, name='remove_ticket_from_booking'),
    path('cancel_booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]
