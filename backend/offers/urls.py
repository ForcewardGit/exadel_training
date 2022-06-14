from django.urls import path
from . import views

urlpatterns = [
    path("", views.OfferList.as_view(), name = "offers"),
    path("<int:pk>/", views.OfferDetail.as_view(), name = "offer"),
    path("<str:username>/", views.user_offers, name = "offers-user"),
]