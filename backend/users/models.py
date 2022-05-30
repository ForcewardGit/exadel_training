from django.db import models
from django.contrib.auth.models import User


class RegularUser(models.Model):
    """ Stores the users which have registered as a regular user in platform.
    """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user}"


class Company(models.Model):
    """ Stores the users which have registered as a company in platform.
    """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    name = models.CharField(max_length=30, unique=True)
    rating = models.FloatField(default=0.0, blank=True)
    cost_per_hour = models.PositiveSmallIntegerField(null=True, blank=True)
    services = models.ManyToManyField('Service')

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
    avg_price = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name