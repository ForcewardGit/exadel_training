from django.db import models
# from service_requests.models import Request


class GeneralUser(models.Model):
    """ Stores all the users registered in platform.
    """
    class Types(models.TextChoices):
        COMPANY = "Company", "company"
        REG_USER = "RegularUser", "regularuser"

    type = models.CharField(max_length=12, choices=Types.choices, default=Types.REG_USER)

    username = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"General user: {self.username}"


class RegularUserFields(models.Model):
    user = models.OneToOneField(GeneralUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    addresses = models.ManyToManyField('Address')

class RegularUserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type = GeneralUser.Types.REG_USER)

class RegularUser(GeneralUser):
    """ Stores the users which have registered as a regular user in platform.
    """
    objects = RegularUserManager()
    
    def save(self, *args, **kwargs):
        # if the record does not exist, specify the type #
        if not self.pk:
            self.type = GeneralUser.Types.REG_USER
        return super().save(*args, **kwargs)
    
    @property
    def fields(self):
        return self.regularuserfields

    def __str__(self):
        return f"Regular user: {self.username}"


class CompanyFields(models.Model):
    user = models.OneToOneField(GeneralUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, unique=True)
    rating = models.FloatField(default=0.0, blank=True)
    cost_per_hour = models.PositiveSmallIntegerField(null=True, blank=True)
    services = models.ManyToManyField('Service')

class CompanyManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type = GeneralUser.Types.COMPANY)

class Company(GeneralUser):
    """ Stores the users which have registered as a company in platform.
    """
    objects = CompanyManager()

    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = GeneralUser.Types.COMPANY
        return super().save(*args, **kwargs)

    @property
    def fields(self):
        return self.companyfields

    def __str__(self):
        return f"Company: {self.name}"


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
    name = models.CharField(max_length=30)
    companies = models.ManyToManyField(Company)
    # requests = models.ManyToManyField(service_requests.models.Request)

    def __str__(self):
        return f"{self.name}"
