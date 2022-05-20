from django.contrib import admin
from .models import RegularUser, Company, Address, Service

admin.site.register(RegularUser)
admin.site.register(Company)
admin.site.register(Address)
admin.site.register(Service)
