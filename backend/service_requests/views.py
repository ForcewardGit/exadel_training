from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from users.models import RegularUser, Company, User
from .models import Request

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView



### CRUD for Request ###
class RequestCreateView(CreateView):
    model = Request
    fields = "__all__"
    template_name = "service_requests/request_form.html"
    success_url = reverse_lazy("requests-users")


class RequestUpdateView(UpdateView):
    model = Request
    fields = "__all__"
    template_name = "service_requests/request_form.html"
    success_url = reverse_lazy("requests-users")


class RequestDeleteView(DeleteView):
    model = Request
    context_object_name = "request"
    success_url = reverse_lazy("requests-users")
    template_name = "service_requests/delete_template.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = self.request.user.username
        return context


def requests_users(request):
    users = RegularUser.objects.all()
    context = {"users": users}
    return render(request, "service_requests/requests.html", context)


class UserRequestListView(ListView):
    template_name = "service_requests/user_requests.html"
    context_object_name = "user_requests"

    def get_queryset(self):
        self.user = get_object_or_404(User, username = self.kwargs["username"])
        self.user = RegularUser.objects.get(user = self.user)
        return Request.objects.filter(user=self.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.user
        return context


class UserRequestDetailView(DetailView):
    model = Request
    context_object_name = "request"
    template_name = "service_requests/user_request.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = kwargs["object"].user.user.username
        return context
