from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("", views.RequestsList.as_view(), name = "requests"),
    path("<int:pk>/", views.RequestDetail.as_view(), name = "request"),
    path("<str:username>/", views.user_requests, name = "user_requests"),
]

urlpatterns = format_suffix_patterns(urlpatterns)