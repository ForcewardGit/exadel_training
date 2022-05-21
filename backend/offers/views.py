from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Offer
from .serializers import OfferSerializer


class OfferList(generics.ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

class OfferDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer