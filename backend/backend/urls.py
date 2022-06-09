from django.contrib import admin
from django.urls import include, path
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt import views as jwt_views

from users.views import services_list, service_detail, service_companies


@api_view(["GET"])
def api_overview(request):
    allowed_urls = {
        "/": "List of allowed urls",
        "/users/": "List of General Users, Allowed methods: ['GET', 'POST']",
        "/users/regular_users/": "List of Regular Users, Allowed methods: ['GET', 'POST']",
        "/users/regular_users/<int:pk>/": "The detail page of a Regular User, Allowed methods: ['GET', 'PUT', 'DELETE']",
        "/users/companies/": "The list of all Companies, Allowed methods: ['GET', 'POST']",
        "/users/companies/<str:name>/": "The details about a Company, Allowed methods: ['GET', 'PUT', 'DELETE']",
        "/users/<str:username>/": "The details of a General User, Allowed methods: ['GET', 'PUT', 'DELETE']",
        "/requests/": "The list of all Requests, Allowed methods: ['GET', 'POST']",
        "/requests/<int:pk>/": "Details about a Request, Allowed methods: ['GET', 'PUT', 'DELETE']",
        "/requests/<str:username>/": "The requests of a user, Allowed methods: ['GET']",
        "/offers/": "The list of all Offers, Allowed methods: ['GET', 'POST']",
        "/offers/<int:pk>/": "The details of an Offer, Allowed methods: ['GET', 'PUT', 'DELETE']",
        "/services/": "The list of all Services, Allowed methods: ['GET', 'POST']",
        "/services/<int:pk>/": "The details of a Service, Allowed methods: ['GET', 'PUT', 'DELETE']",
        "/services/<int:pk>/companies/": "The list of Companies providing a Service, Allowed methods: ['GET']",
    }

    return Response(allowed_urls)



urlpatterns = [
    path("", api_overview),
    path('admin/', admin.site.urls),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path("users/", include("users.urls")),
    path("requests/", include("service_requests.urls")),
    path("offers/", include("offers.urls")),

    path("services/", services_list, name = "services"),
    path("services/<int:pk>/", service_detail, name = "service_detail"),
    path("services/<int:pk>/companies/", service_companies, name = "service_companies"),
]
