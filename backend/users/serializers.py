from rest_framework.serializers import ModelSerializer
from .models import User, RegularUser, Company, Service


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class RegularUserSerializer(ModelSerializer):
    class Meta:
        model = RegularUser
        fields = "__all__"

class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"