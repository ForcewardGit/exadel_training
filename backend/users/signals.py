from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from .models import User, RegularUser, Company


####### Signals handling ##########
@receiver(post_save, sender = RegularUser)
def update_regular_user(sender, instance, created, **kwargs):
    """ Function will be called when updating regular user, 
        to update possible fields of general user as well.
    """
    if not created:
        regular_user = instance
        user = regular_user.user
        user.first_name = regular_user.name
        user.last_name = regular_user.surname
        user.save()
