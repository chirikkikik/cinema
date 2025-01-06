from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking, Ticket
from movies.models import Screening
from payments.models import Payment

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
    booking = Booking.objects.filter(user=request.user, screening=screening, status='Pending').first()
    
    if not booking:
        booking = Booking.objects.create(
            user=request.user,
            screening=screening,
            status='Pending'
        )

    all_tickets = Ticket.objects.filter(screening=screening)
    taken_seats = all_tickets.filter(is_booked=True).values_list('seat', flat=True)

    error_message = None
    if request.method == 'POST':
        seat = request.POST.get('seat')
        ticket = all_tickets.filter(seat=seat).first()

        if not ticket:
            error_message = "Некоректний номер місця. Будь ласка, введіть назву місця у форматі 'A1'."
        elif ticket.is_booked:
            error_message = "Це місце вже зайняте. Будь ласка, виберіть інше."
        else:
            ticket.is_booked = True
            screening.decrease_seat()
            ticket.save()
            booking.tickets_booked.add(ticket)
            return redirect('booking_summary', booking_id=booking.id)

    context = {
        'screening': screening,
        'booking': booking,
        'taken_seats': taken_seats,
        'error_message': error_message,
    }
    return render(request, 'choose_seat.html', context)


@login_required(login_url='/login/')
def booking_summary(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user, status='pending')

    if request.method == 'POST':
        if 'remove_ticket' in request.POST:
            ticket_id = request.POST.get('ticket_id')
            return remove_ticket_from_booking(request, ticket_id)
        elif 'confirm_booking' in request.POST:
            booking.status = 'confirmed'
            booking.save()
            messages.success(request, "Ваше бронювання підтверджено.")
            return redirect('user_profile')

    context = {
        'booking': booking,
        'tickets': booking.tickets_booked.all(),
        'total_cost': booking.total_cost(),
    }
    return render(request, 'booking_summary.html', context)


@login_required(login_url='/login/')
def remove_ticket_from_booking(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, is_booked=True)
    booking = Booking.objects.filter(tickets_booked=ticket, user=request.user, status='pending').first()
    
    if not booking:
        messages.error(request, "Квиток не належить до жодного з ваших активних бронювань.")
        return redirect('user_profile')

    booking.remove_ticket(ticket)
    
    if not booking.tickets_booked.exists():
        booking.delete()
        return redirect('home_page')

    messages.success(request, "Квиток успішно видалено.")
    return redirect('booking_summary', booking_id=booking.id)


@login_required(login_url='/login/')
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user, status='pending')
    
    for ticket in booking.tickets_booked.all():
        if ticket.is_booked:
            ticket.is_booked = False
            ticket.save()
            
    booking.delete()
    
    messages.info(request, "Ваше бронювання успішно скасовано.")
    return redirect('user_profile')









