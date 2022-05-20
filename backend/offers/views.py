from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Offer
from .serializers import OfferSerializer


@api_view(["GET"])
def offers_list(request):
    offers = Offer.objects.all()
    serializer = OfferSerializer(offers, many = True)

    return Response(serializer.data)


@api_view(["GET"])
def offer_detail(request, pk):
    offer = Offer.objects.get(id=pk)
    serializer = OfferSerializer(offer, many = False)

    return Response(serializer.data)
    

@api_view(["POST"])
def create_offer(request):
    serializer = OfferSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["POST"])
def update_offer(request, pk):
    offer = Offer.objects.get(id=pk)
    serializer = OfferSerializer(data = request.data, instance = offer)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["POST"])
def delete_offer(request, pk):
    offer = Offer.objects.get(id=pk)
    offer.delete()

    return Response("Offer is deleted successfully!")