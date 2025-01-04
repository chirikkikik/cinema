from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from bookings.models import Booking
from .forms import CustomLoginForm, RegistrationForm
from payments.models import Payment

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login') 
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_superuser:
                return redirect('/admin/')
            return redirect('/')
        else:
            messages.error(request, 'Невірний логін або пароль.')
    else:
        form = CustomLoginForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/login/')
def user_profile(request):
    user = request.user
    bookings = Booking.objects.filter(user=user)
    error_message = None

    if request.method == 'POST':
        action = request.POST.get('action')
        booking_id = request.POST.get('booking_id')

        try:
            booking = Booking.objects.get(id=booking_id, user=user)
        except Booking.DoesNotExist:
            error_message = "Бронювання не знайдено."
            bookings = Booking.objects.filter(user=user)
            return render(request, 'user_profile.html', {'bookings': bookings, 'error_message': error_message})

        if action == 'pay':
            if not booking.is_paid:
                Payment.objects.create(
                    user=user,
                    booking=booking,
                    amount=booking.total_cost(),
                    status='completed'
                )
                booking.is_paid = True
                booking.save()
                messages.success(request, "Оплата успішно завершена.")
            else:
                error_message = "Це бронювання вже оплачено."

        elif action == 'delete':
            if not booking.is_paid:
                for ticket in booking.tickets_booked.all():
                    booking.remove_ticket(ticket)
                booking.delete()
                messages.success(request, "Бронювання успішно видалено.")
            else:
                error_message = "Оплачене бронювання не можна видалити."

    bookings = Booking.objects.filter(user=user)
    context = {
        'bookings': bookings,
        'error_message': error_message,
    }
    return render(request, 'user_profile.html', context)


    