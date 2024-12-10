from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from bookings.models import Booking
from .models import Payment
from django.contrib import messages

@login_required
def payment_form(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user, is_paid=False)
    
    if request.method == 'POST':
        payment = Payment.objects.create(
            user=request.user,
            booking=booking,
            amount=booking.total_cost(),
        )
        
        payment.status = 'completed'
        payment.save()

        booking.is_paid = True
        booking.save()

        messages.success(request, "Оплата успішно завершена.")
        return redirect('payment_success')
    
    return render(request, 'payment_form.html', {'booking': booking})

@login_required
def payment_success(request):
    return render(request, 'payment_success.html')
