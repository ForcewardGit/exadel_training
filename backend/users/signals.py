from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import RegularUser, Company


####### Signals handling ##########
@receiver(post_save, sender = RegularUser)
def update_regular_user(sender, instance, created, **kwargs):
    """ Function will be called when updating regular user, 
        to update possible fields of general user as well.
    """
    if not created:
        regular_user = instance
        user = regular_user.user
        user.username = regular_user.username
        user.password = regular_user.password
        user.first_name = regular_user.name
        user.last_name = regular_user.surname
        user.save()


@receiver(post_save, sender = Company)
def update_company(sender, instance, created, **kwargs):
    """ Function will be called when updating regular user, 
        to update possible fields of general user as well.
    """
    if not created:
        company = instance
        user = company.user
        user.username = company.username
        user.password = company.password
        user.save()
