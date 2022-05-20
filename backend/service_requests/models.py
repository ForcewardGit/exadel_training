from django.db import models
from users.models import Company, RegularUser, Address, Service


class Request(models.Model):
    date = models.DateTimeField(auto_now=True)
    total_area = models.FloatField()
    
    user = models.ForeignKey(RegularUser, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Request {self.id}"


class Notification(models.Model):
    time = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    request = models.OneToOneField(Request, on_delete=models.CASCADE)

    def __str__(self):
        company = Company.objects.get(id = self.company)
        return f"{company.name}: {self.time}"
