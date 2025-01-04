from random import uniform
from movies.models import Screening
from .models import Ticket

def populate_tickets():
    Ticket.objects.all().delete()
    tickets_data = []

    for screening in Screening.objects.all():
        for row in ['A', 'B', 'C']:
            for seat_number in range(1, 11):
                tickets_data.append(Ticket(
                    screening=screening,
                    price=uniform(100, 300),
                    seat=f"{row}{seat_number}",
                    is_booked=False
                ))

    Ticket.objects.bulk_create(tickets_data)
    print(f"Створено {len(tickets_data)} квитків.")

if __name__ == "__main__":
    populate_tickets()
