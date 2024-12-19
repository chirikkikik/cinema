from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from bookings.models import Booking
from .models import Payment
from django.contrib import messages

@login_required(login_url='/login/')
def payment_form(request, booking_id):
    try:
        booking = Booking.objects.get(id=booking_id, user=request.user)
    except Booking.DoesNotExist:
        messages.error(request, "Бронювання не знайдено.")
        return redirect('choose_screening')

    if request.method == 'POST':
        if not Payment.objects.filter(booking=booking).exists():
            payment = Payment.objects.create(
                user=request.user,
                booking=booking,
                amount=booking.total_cost(),
                status='completed'
            )
            messages.success(request, "Оплата успішно завершена.")
            return redirect('payment_success')

    context = {'booking': booking}
    return render(request, 'payment_form.html', context)


@login_required
def payment_success(request):
    return render(request, 'payment_success.html')