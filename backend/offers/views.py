from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .permissions import OfferOwnerPermission
from .models import Offer
from .serializers import OfferSerializer
from users.models import RegularUser


class OfferList(ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [IsAuthenticated | IsAdminUser]


class OfferDetail(RetrieveUpdateDestroyAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [IsAuthenticated, OfferOwnerPermission | IsAdminUser]


@api_view(["GET"])
@permission_classes([IsAuthenticated | IsAdminUser])
def user_offers(request, username):
    try:
        user = RegularUser.objects.get(username = username)
    except RegularUser.DoesNotExist:
        return Response(status = 404)

    if request.user.id == user.user.id or request.user.is_staff:
        offers = Offer.objects.filter(user = user)
        serializer = OfferSerializer(offers, many = True)

        return Response(serializer.data, status = 200)
    
    return Response(status = 403)
