from django.db import models
from users.models import RegularUser, Company


class Offer(models.Model):
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(RegularUser, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"User: {self.user} - Company: {self.company}"
