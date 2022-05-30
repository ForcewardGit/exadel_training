from django.urls import path
from .views import RequestDeleteView, UserRequestListView, UserRequestDetailView, RequestCreateView, RequestUpdateView, requests_users

urlpatterns = [    
    path("create/", RequestCreateView.as_view(), name = "requests-create"),
    path("update/<int:pk>/", RequestUpdateView.as_view(), name = "requests-update"),
    path("delete/<int:pk>/", RequestDeleteView.as_view(), name = "requests-delete"),

    path("", requests_users, name = "requests-users"),
    path("<int:pk>/", UserRequestDetailView.as_view(), name = "requests-user_request"),
    path("<str:username>/", UserRequestListView.as_view(), name = "requests-user_requests"),
]
