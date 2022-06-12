from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import OfferOwnerPermission

from .models import Offer
from .serializers import OfferSerializer


class OfferList(ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [IsAuthenticated]


class OfferDetail(RetrieveUpdateDestroyAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [IsAuthenticated, OfferOwnerPermission | IsAdminUser]
