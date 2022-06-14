from django.db import models
from django.contrib.auth.models import User


class RegularUser(models.Model):
    """ Stores the users which have registered as a regular user in platform.
    """
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=50, null=True)
    surname = models.CharField(max_length=50, null=True)

    def save(self, *args, **kwargs):
        try:
            User.objects.get(username = self.username)
            super().save(*args, **kwargs)
        except User.DoesNotExist:
            general_user = User.objects.create_user(username = self.username, password = self.password)
            self.user = general_user
            super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Company(models.Model):
    """ Stores the users which have registered as a company in platform.
    """
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=30, unique=True)
    rating = models.FloatField(default=0.0, blank=True)
    cost_per_hour = models.PositiveSmallIntegerField(null=True, blank=True)
    services = models.ManyToManyField('Service', null=True, blank=True, related_name="services")

    def save(self, *args, **kwargs):
        try:
            User.objects.get(username = self.username)
        except User.DoesNotExist:
            general_user = User.objects.create(username = self.username, password = self.password)
            self.user = general_user
            super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class Address(models.Model):
    """ Stores the addresses of regular users.
    """
    user_id = models.ForeignKey(RegularUser, on_delete=models.CASCADE)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    house_number = models.PositiveSmallIntegerField()
    ap_number = models.PositiveSmallIntegerField() # apartment number

    def __str__(self):
        return f"{self.ap_number}, {self.house_number}, {self.street}, {self.city}, {self.country}"


class Service(models.Model):
    """ Stores the types of services that companies may provide.
    """
    name = models.CharField(max_length=30)
    avg_price = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return self.name


class Notification(models.Model):
    """ Stores all the notifications for Users
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    sent_time = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user} - {self.sent_time} - {self.read}"
