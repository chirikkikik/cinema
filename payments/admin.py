from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('booking', 'amount', 'payment_date', 'status', 'transaction_id')
    list_filter = ('status', 'payment_date')
    search_fields = ('transaction_id', 'booking__user__username')

