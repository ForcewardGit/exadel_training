from rest_framework.serializers import ModelSerializer
from .models import User, RegularUser, Company, Service


class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            "password": {"write_only": True},
        }
    
    def create(self, validated_data):
        user = User.objects.create_user(validated_data["username"], password = validated_data["password"])
        return user


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
