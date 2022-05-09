from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from .models import GeneralUser, RegularUser, Company, Service


class GeneralUsersView(View):
    def get(self, request):
        all_users = GeneralUser.objects.all()
        return render(request, "users/general_users.html", {"users": all_users})

def user_details(request, username):
    user = GeneralUser.objects.get(username=username)
    return render(request, "users/general_user_details.html", {"user": user})


def company_details(request, name):
    company = Company.objects.get(name = name)
    return company


def regular_user_details(request, pk):
    user = RegularUser.objects.get(id = pk)
    return user


class ServiceListView(ListView):
    model = Service
    context_object_name = "services"
    template_name = "users/services.html"


class ServiceDetailView(DetailView):
    model = Service
    context_object_name = "service"
    template_name = "users/service.html"


def service_companies(request, pk):
    service = Service.objects.get(id=pk)
    filtered_companies = Company.objects.filter(services__id = service.id)
    context = {"companies": filtered_companies, "service": service}

    return render(request, "users/service_companies.html", context)
    