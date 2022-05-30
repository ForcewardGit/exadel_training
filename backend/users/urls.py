from django.urls import path
from . import views

urlpatterns = [
    path("", views.GeneralUsersView.as_view(), name="general_users"),
    path("regular_users/", views.RegularUserListView.as_view(), name = "users-regular_users"),
    path("regular_users/<int:pk>/", views.RegularUserDetailView.as_view(), name = "users-regular_user"),
    path("<str:username>/", views.user_details, name = "general_users-detail"),
    path("companies/<str:name>/", views.company_details, name = "users-company_details"),
]