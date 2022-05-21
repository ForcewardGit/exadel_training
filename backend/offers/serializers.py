from rest_framework import serializers
from users.models import RegularUser, Company
from .models import Offer


class OfferSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    date = serializers.DateTimeField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=RegularUser.objects.all())
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())

    def create(self, validated_data):
        return Offer.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.company = validated_data.get('company', instance.company)
        instance.save()
        return instance
