from rest_framework.permissions import BasePermission
from .models import User, Company, RegularUser


class GeneralUserPermission(BasePermission):
    def has_permission(self, request, view):
        requested_user_username = view.kwargs.get("username")
        if requested_user_username is None:
            return False
        return request.user.username == requested_user_username


class RegularUserPermission(BasePermission):
    def has_permission(self, request, view):
        requested_user_id = view.kwargs.get('pk')
        if requested_user_id is None:
            return False
        return RegularUser.objects.get(pk = requested_user_id).user.id == request.user.id


class CompanyPermission(BasePermission):
    def has_permission(self, request, view):
        company_name = view.kwargs.get('name')
        if company_name is None:
            return False
        return Company.objects.get(name=company_name).user.id == request.user.id
