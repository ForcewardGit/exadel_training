from rest_framework.serializers import ModelSerializer
from .models import User, RegularUser, Company, Service


class RegularUserRegisterSerializer(ModelSerializer):
    class Meta:
        model = RegularUser
        fields = "__all__"
        extra_kwargs = {
            "password": {"write_only": True},
        }
    
    def create(self, validated_data):
        user = RegularUser.objects.create(
            username = validated_data["username"],
            password = validated_data["password"],
            name = validated_data["name"],
            surname = validated_data["surname"],
        )
        return user


class CompanyRegisterSerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
        extra_kwargs = {
            "password": {"write_only": True},
        }
    
    def create(self, validated_data):
        company = Company.objects.create(
            username = validated_data["username"],
            password = validated_data["password"],
            name = validated_data["name"],
            surname = validated_data["surname"],
            rating = validated_data["rating"],
            cost_per_hour = validated_data["cost_per_hour"],
        )
        return company


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
