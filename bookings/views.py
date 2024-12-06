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
    booking = Booking.objects.filter(user=request.user, is_paid=False).first()
    
    if not booking:
        booking = Booking.objects.create(user=request.user)
        messages.info(request, "Створено нове бронювання.")
        
    screening = get_object_or_404(Screening, id=screening_id)

    if request.method == 'POST':
        row = request.POST.get('row')
        number = request.POST.get('number')

        ticket = Ticket.objects.filter(screening=screening, row=row, number=number).first()
        if not ticket:
            return HttpResponse("Цього місця нема в цій аудиторії", status=400)
        if ticket.is_booked:
            return HttpResponse("Це місце вже заброньоване.", status=400)
        
        ticket.is_booked = True
        ticket.save()

        booking.tickets.add(ticket)
        return redirect('booking_summary', booking_id=booking.id)

    context = {
        'screening': screening,
        'booking': booking,
    }
    return render(request, 'choose_seat.html', context)

@login_required(login_url='/login/')
def booking_summary(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user, is_paid=False)

    if not booking.tickets.exists():
        messages.info(request, "У вас немає квитків у цьому бронюванні.")
        return redirect('choose_screening')

    context = {
        'booking': booking,
        'tickets': booking.tickets.all(),
        'total_cost': booking.total_cost(),
    }
    return render(request, 'booking/booking_summary.html', context)

@login_required(login_url='/login/')
def remove_ticket_from_booking(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, booking__is_paid=False, booking__user=request.user)

    ticket.is_booked = False
    ticket.save()

    ticket.delete()

    messages.success(request, "Квиток успішно видалено з вашого бронювання.")
    return redirect('booking_summary', booking_id=ticket.booking.id)
