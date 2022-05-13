from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import User, RegularUser, Company, Service



def index(request):
    context = {
        "users": RegularUser.objects.all(),
        "companies": Company.objects.all(),
        "services": Service.objects.all(),
    }

    return render(request, "users/index.html", context)


class GeneralUsersView(View):
    """ General Users View """
    def get(self, request):
        all_users = User.objects.all()
        return render(request, "users/general_users.html", {"users": all_users})


def user_details(request, username):
    """ General User Details View """
    user = User.objects.get(username=username)
    return render(request, "users/general_user_details.html", {"user": user})


def company_details(request, name):
    company = Company.objects.get(name = name) # name is unique field for companies
    context = {"company": company}

    return render(request, "users/company_details.html", context)


class RegularUserListView(ListView):
    model = RegularUser
    context_object_name = "users"
    template_name = "users/regular_users.html"


class RegularUserDetailView(DetailView):
    model = RegularUser
    context_object_name = "user"
    template_name = "users/regular_user.html"


class ServiceListView(ListView):
    model = Service
    context_object_name = "services"
    template_name = "services/services.html"


class ServiceDetailView(DetailView):
    model = Service
    context_object_name = "service"
    template_name = "services/service.html"


class ServiceCreateView(CreateView):
    model = Service
    fields = "__all__"
    template_name = "services/services_form.html"
    success_url = reverse_lazy('services')


class ServiceUpdateView(UpdateView):
    model = Service
    fields = "__all__"
    template_name = "services/services_form.html"
    success_url = reverse_lazy('services')


class ServiceDeleteView(DeleteView):
    model = Service
    context_object_name = "service"
    success_url = reverse_lazy('services')
    template_name = "services/service_confirm_delete.html"


def service_companies(request, pk):
    service = Service.objects.get(id=pk)
    filtered_companies = Company.objects.filter(services__id = service.id)
    context = {"companies": filtered_companies, "service": service}

    return render(request, "services/service_companies.html", context)
