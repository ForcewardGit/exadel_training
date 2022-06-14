from django.urls import path
from . import views

urlpatterns = [
    path("", views.general_users, name = "general_users"),
    path("register/regular_user/", views.register_regular_user, name = "register-regular-user"),
    path("register/company_user/", views.register_company_user, name = "register-company-user"),
    path("regular_users/", views.regular_users, name = "users-regular_users"),
    path("regular_users/<int:pk>/", views.regular_user, name = "users-regular_user"),

    path("companies/", views.companies_list, name = "users-companies"),
    path("companies/<str:name>/", views.company_details, name = "users-company_details"),

    path("<str:username>/", views.user_details, name = "general_users-detail"),
]