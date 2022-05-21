from rest_framework import serializers
from .models import User, Service, RegularUser, Company


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=150)

    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.save()
        return instance


class RegularUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    surname = serializers.CharField(max_length=50)
    user = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=User.objects.all(), required=False)

    def create(self, validated_data):
        return RegularUser.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.user = validated_data.get('user', instance.user)
        instance.services = validated_data.get("services", instance.services)
        instance.save()
        return instance


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField(max_length=30)
    rating = serializers.FloatField(required=False)
    cost_per_hour = serializers.IntegerField(allow_null=True, required=False)
    user = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=User.objects.all(), required=False)
    services = serializers.PrimaryKeyRelatedField(allow_null=True, many=True, queryset=Service.objects.all(), required=False)

    def create(self, validated_data):
        return Company.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.cost_per_hour = validated_data.get('cost_per_hour', instance.cost_per_hour)
        instance.user = validated_data.get('user', instance.user)
        instance.save()
        return instance


class ServiceSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField(max_length=30)
    avg_price = serializers.IntegerField(allow_null=True, required=False)

    def create(self, validated_data):
        return Service.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.avg_price = validated_data.get('avg_price', instance.avg_price)
        instance.save()
        return instance