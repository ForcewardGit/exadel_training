from django.urls import path
from . import views

urlpatterns = [
    path("", views.GeneralUsersView.as_view(), name="general_users"),
    path("<str:username>/", views.user_details, name = "users-detail"),
    path("companies/<str:name>/", views.company_details, name = "users-company_details"),
    path("regular_users/<int:pk>/", views.regular_user_details, name = "users-regular_user_details"),
]