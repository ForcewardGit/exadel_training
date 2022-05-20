from django.urls import path
from . import views

urlpatterns = [    
    path("create/", views.create_request, name = "requests-create"),
    path("update/<int:pk>/", views.update_request, name = "requests-update"),
    path("delete/<int:pk>/", views.delete_request, name = "requests-delete"),

    path("", views.all_requests, name = "requests"),
    path("<int:pk>/", views.request_detail, name = "request"),
    path("<str:username>/", views.user_requests, name = "user_requests"),
]