from django.db import models


class GeneralUser(models.Model):
    """ Stores all the users registered in platform.
    """
    username = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.username}"


class RegularUser(models.Model):
    """ Stores the users which have registered as a regular user in platform.
    """
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    username = models.OneToOneField(to=GeneralUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.username}"


class Company(models.Model):
    """ Stores the users which have registered as a company in platform.
    """
    name = models.CharField(max_length=30, unique=True)
    rating = models.FloatField(default=0.0, blank=True)
    cost_per_hour = models.PositiveSmallIntegerField(null=True, blank=True)
    services = models.ManyToManyField('Service')
    username = models.OneToOneField(to=GeneralUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Address(models.Model):
    """ Stores the addresses of regular users.
    """
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    house_number = models.PositiveSmallIntegerField()
    ap_number = models.PositiveSmallIntegerField() # apartment number
    user_id = models.ForeignKey(RegularUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ap_number}, {self.house_number}, {self.street}, {self.city}, {self.country}"


class Service(models.Model):
    """ Stores the types of services that companies may provide.
    """
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
