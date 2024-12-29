from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking, Ticket
from movies.models import Screening, Movie

@login_required(login_url='/login/')
def choose_screening(request, movie_id):
    screenings = Screening.objects.filter(movie_id=movie_id)
    context = {
        'screenings': screenings,
    }
    return render(request, 'choose_screening.html', context)


@login_required(login_url='/login/')
def choose_seat(request, screening_id):
    screening = get_object_or_404(Screening, id=screening_id)
    booking, created = Booking.objects.get_or_create(
        user=request.user,
        screening=screening,
        status='Pending'
    )
    if created:
        messages.info(request, "Створено нове бронювання.")

    all_tickets = Ticket.objects.filter(screening=screening)
    taken_seats = all_tickets.filter(is_booked=True).values_list('seat', flat=True)

    if request.method == 'POST':
        seat = request.POST.get('seat')
        ticket = all_tickets.filter(seat=seat).first()
        if not ticket:
            messages.error(request, "Некоректний номер місця.")
        elif ticket.is_booked:
            messages.error(request, "Це місце вже зайняте.")
        else:
            ticket.is_booked = True
            ticket.save()
            booking.tickets_booked.add(ticket)
            messages.success(request, f"Місце {seat} успішно заброньовано.")
            return redirect('booking_summary', booking_id=booking.id)

    context = {
        'screening': screening,
        'booking': booking,
        'taken_seats': taken_seats,
    }
    return render(request, 'choose_seat.html', context)


@login_required(login_url='/login/')
def booking_summary(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user, status='Pending')

    if not booking.tickets_booked.exists():
        messages.info(request, "У вас немає квитків у цьому бронюванні.")
        return redirect('choose_screening', movie_id=booking.screening.movie.id)

    if request.method == 'POST':
        return redirect('payment_form', booking_id=booking.id)

    context = {
        'booking': booking,
        'tickets': booking.tickets_booked.all(),
        'total_cost': booking.total_cost(),
    }
    return render(request, 'booking_summary.html', context)



@login_required(login_url='/login/')
def remove_ticket_from_booking(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, is_booked=True)
    booking = Booking.objects.filter(tickets_booked=ticket, user=request.user).first()
    
    if not booking:
        messages.error(request, "Бронювання для цього квитка не знайдено або квиток вам не належить.")
        return redirect('choose_screening')

    booking.tickets_booked.remove(ticket)
    ticket.is_booked = False
    ticket.save()
    
    screening = ticket.screening
    screening.available_seats += 1
    screening.save()

    messages.success(request, "Квиток успішно видалено з вашого бронювання.")
    return redirect('booking_summary', booking_id=booking.id)







