from rest_framework import serializers
from .models import Request
from users.models import RegularUser, Company, Address, Service


class RequestSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    date = serializers.DateTimeField(read_only=True)
    total_area = serializers.FloatField()
    user = serializers.PrimaryKeyRelatedField(queryset=RegularUser.objects.all())
    service = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all())
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
    address = serializers.PrimaryKeyRelatedField(queryset=Address.objects.all())

    def create(self, validated_data):
        print(validated_data)
        return Request.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        print(validated_data)
        instance.total_area = validated_data.get('total_area', instance.total_area)
        instance.user = validated_data.get('user', instance.user)
        instance.service = validated_data.get('service', instance.service)
        instance.company = validated_data.get('company', instance.company)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance