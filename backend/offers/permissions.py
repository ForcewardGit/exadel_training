from rest_framework.permissions import BasePermission
from .models import Offer


class OfferOwnerPermission(BasePermission):
    def has_permission(self, request, view):
        requested_offer_id = view.kwargs.get("pk")
        if requested_offer_id is None:
            return False
        return request.user.id == Offer.objects.get(pk=requested_offer_id).user.user.id