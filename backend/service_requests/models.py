from django.db import models
from users.models import Company, RegularUser, Address


class Request(models.Model):
    date = models.DateTimeField(auto_now=True)
    total_area = models.FloatField()
    user = models.ForeignKey(RegularUser, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    # company_services = [(s, s) for s in company.services.all()]
    service = models.CharField(max_length=30)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.id


class Notification(models.Model):
    time = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    request = models.OneToOneField(Request, on_delete=models.CASCADE)

    def __str__(self):
        company = Company.objects.get(id = self.company)
        return f"{company.name}: {self.time}"
