from django.shortcuts import render

'''
def confirm_booking(self):
        if not self.is_confirmed:
            self.is_confirmed = True
            self.save()
            self.screening.audit.free_seats -= 1
            self.screening.audit.save()
    
@receiver(post_delete, sender=Booking)
def delete_booking(sender, instance, **kwargs):
    if instance.is_confirmed:
        instance.screening.audit.free_seats += 1
        instance.screening.audit.save()
'''
