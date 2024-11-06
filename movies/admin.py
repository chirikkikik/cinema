from django.contrib import admin
from .models import Movie, Cinema, Audit, Screening, Seat

admin.site.register(Movie)
admin.site.register(Cinema)
admin.site.register(Audit)
admin.site.register(Screening)
admin.site.register(Seat)


