from django.contrib import admin
from django.urls import include, path
from rest_framework.response import Response
from rest_framework.decorators import api_view

from users.views import services_list, service_detail, create_service, update_service, delete_service, service_companies


@api_view(["GET"])
def api_overview(request):
    allowed_urls = {
        "/": "List of allowed urls",
        "/users/": "List of General Users",
        "/users/regular_users/": "List of Regular Users",
        "/users/regular_users/<int:pk>/": "The detail page of a Regular User",
        "/users/companies/": "The list of all Companies",
        "/users/companies/create/": "Create a Company",
        "/users/companies/update/<str:name>/": "Update a Company",
        "/users/companies/delete/<str:name>/": "Delete a Company",
        "/users/companies/<str:name>/": "The details about a Company",
        "/users/<str:username>/": "The details of a General User",
        "/requests/": "The list of all Requests",
        "/requests/create/": "Create a Request",
        "/requests/update/<int:pk>/": "Update a Request",
        "/requests/delete/<int:pk>/": "Delete a Request",
        "/requests/<int:pk>/": "Details about a Request",
        "/requests/<str:username>/": "The requests of a user",
        "/offers/": "The list of all Offers",
        "/offers/create/": "Create an Offer",
        "/offers/update/<int:pk>/": "Update an Offer",
        "/offers/delete/<int:pk>/": "Delete an Offer",
        "/offers/<int:pk>/": "The details of an Offer",
        "/services/": "The list of all Services",
        "/services/<int:pk>/": "The details of a Service",
        "/services/create/": "Create a Service",
        "/services/<int:pk>/update/": "Update a Service",
        "/services/<int:pk>/delete/": "Delete a Service",
        "/services/<int:pk>/companies/": "The list of Companies providing a Service",
    }

    return Response(allowed_urls)



urlpatterns = [
    path("", api_overview),
    path('admin/', admin.site.urls),

    path("users/", include("users.urls")),
    path("requests/", include("service_requests.urls")),
    path("offers/", include("offers.urls")),

    path("services/", services_list, name = "services"),
    path("services/<int:pk>/", service_detail, name = "service_detail"),
    path("services/create/", create_service, name = "services-create"),
    path("services/<int:pk>/update/", update_service, name = "services-update"),
    path("services/<int:pk>/delete/", delete_service, name = "services_delete"),
    path("services/<int:pk>/companies/", service_companies, name = "service_companies"),
]
