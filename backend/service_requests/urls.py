from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


request_list = views.RequestViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
request_detail = views.RequestViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
user_requests = views.RequestViewSet.as_view({
    'get': 'user_requests'
})

urlpatterns = [
    path("", request_list, name = "requests"),
    path("<int:pk>/", request_detail, name = "request"),
    path("<str:username>/", user_requests, name = "user_requests"),
]

urlpatterns = format_suffix_patterns(urlpatterns)