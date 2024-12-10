from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking, Ticket
from movies.models import Screening

@login_required(login_url='/login/')
def choose_screening(request):
    screenings = Screening.objects.all()
    context = {
        'screenings': screenings, 
    }
    return render(request, 'choose_screening.html', context)


@login_required(login_url='/login/')
def choose_seat(request, screening_id):
    screening = get_object_or_404(Screening, id=screening_id)
    booking = Booking.objects.filter(user=request.user, status='Pending').first()
    
    if not booking:
        booking = Booking.objects.create(user=request.user, screening=screening, status='Pending')
        messages.info(request, "Створено нове бронювання.")

    if request.method == 'POST':
        seat = request.POST.get('seat')

        if Ticket.objects.filter(screening=screening, seat=seat).exists():
            messages.error(request, "Це місце вже зайняте.")
            return redirect('choose_seat', screening_id=screening.id)

        ticket = Ticket.objects.create(
            screening=screening,
            price=100.00, 
            seat=seat,
            is_booked=True
        )
        booking.tickets_booked.add(ticket)

        messages.success(request, f"Місце {seat} заброньовано.")
        return redirect('booking_summary', booking_id=booking.id)

    taken_seats = Ticket.objects.filter(screening=screening).values_list('seat', flat=True)
    
    context = {
        'screening': screening,
        'booking': booking,
        'taken_seats': taken_seats,
    }
    return render(request, 'choose_seat.html', context)

@login_required(login_url='/login/')
def booking_summary(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user, status = 'Pending')

    if not booking.tickets_booked.exists():
        messages.info(request, "У вас немає квитків у цьому бронюванні.")
        return redirect('choose_screening')

    context = {
        'booking': booking,
        'tickets': booking.tickets_booked.all(),
        'total_cost': booking.total_cost(),
    }
    return render(request, 'booking_summary.html', context)

@login_required(login_url='/login/')
def remove_ticket_from_booking(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, booking__is_paid=False, booking__user=request.user)

    
    ticket.seat = ''
    ticket.is_booked = False
    ticket.save()

    ticket.delete()

    messages.success(request, "Квиток успішно видалено з вашого бронювання.")
    
    return redirect('booking_summary', booking_id=ticket.booking.id)



