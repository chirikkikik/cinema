from datetime import date, time, timedelta
from movies.models import Movie, Screening
from random import randint, choice


def populate_screenings():
    Screening.objects.all().delete()
    screenings_data = []
    today = date.today()

    for movie in Movie.objects.all():
        for i in range(2):
            screenings_data.append({
                'movie': movie,
                'start_time': time(randint(10,20), 0),
                'date': today + timedelta(days=randint(1, 4)),
                'available_seats': 30,
                'cinema_hall': f"Hall {choice([1, 2])}"
            })

    Screening.objects.bulk_create([Screening(**data) for data in screenings_data])
    print("Screenings populated successfully.")

if __name__ == "__main__":
    populate_screenings()
