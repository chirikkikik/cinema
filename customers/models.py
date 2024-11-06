from django.db import models

class Customer(models.Model):
    user = models.OneToOneField('auth.User', on_delete = models.CASCADE)
    first_name = models.TextField(default='')
    last_name = models.TextField(default='')
    email = models.EmailField(default=(""), max_length = 254)
    
    class Meta:
        db_table = 'Customers'
