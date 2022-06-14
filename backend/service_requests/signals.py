from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import Notification
from .models import Request


@receiver(post_save, sender = Request)
def create_notification(sender, instance, created, **kwargs):
    user = instance.company.user
    Notification.objects.create(user = user)
