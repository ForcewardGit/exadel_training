from django.urls import path
from . import views

urlpatterns = [
    path("", views.offers_list, name = "offers"),
    path("create/", views.create_offer, name = "offers-create"),
    path("update/<int:pk>/", views.update_offer, name = "offers-update"),
    path("delete/<int:pk>/", views.delete_offer, name = "offers-delete"),
    path("<int:pk>/", views.offer_detail, name = "offer"),
]