from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['user', 'booking', 'amount', 'payment_date', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
