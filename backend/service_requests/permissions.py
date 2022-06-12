from rest_framework.permissions import BasePermission
from .models import Request


class RequestOwnerPermission(BasePermission):
    def has_permission(self, request, view):
        requested_request_id = view.kwargs.get("pk")
        if requested_request_id is None:
            return False
        return request.user.id == Request.objects.get(pk=requested_request_id).user.user.id