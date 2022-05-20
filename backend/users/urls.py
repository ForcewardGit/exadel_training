from django.urls import path
from . import views

urlpatterns = [
    path("", views.general_users, name = "general_users"),
    path("regular_users/", views.regular_users, name = "users-regular_users"),
    path("regular_users/<int:pk>/", views.regular_user, name = "users-regular_user"),

    path("companies/", views.companies_list, name = "users-companies"),
    path("companies/create/", views.create_company, name = "users-companies-create"),
    path("companies/update/<str:name>/", views.update_company, name = "users-companies-update"),
    path("companies/delete/<str:name>/", views.delete_company, name = "users-companies-delete"),
    path("companies/<str:name>/", views.company_details, name = "users-company_details"),

    path("<str:username>/", views.user_details, name = "general_users-detail"),
]