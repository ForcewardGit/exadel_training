from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import Notification
from .models import Offer


@receiver(post_save, sender = Offer)
def create_notification(sender, instance, created, **kwargs):
    user = instance.user.user
    Notification.objects.create(user = user)
