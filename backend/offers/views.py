from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from .models import Offer
from .serializers import OfferSerializer


class OfferList(ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

class OfferDetail(RetrieveUpdateDestroyAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    def put(self, request, *args, **kwargs):
        if request.user == self.get_object().user.user or request.user.is_staff:
            return RetrieveUpdateDestroyAPIView.put(self, request, *args, **kwargs)
        return Response(status=401)
    
    def delete(self, request, *args, **kwargs):
        if request.user == self.get_object().user.user or request.user.is_staff:
            return RetrieveUpdateDestroyAPIView.delete(self, request, *args, **kwargs)
        return Response(status=401)
    
    def patch(self, request, *args, **kwargs):
        if request.user == self.get_object().user.user or request.user.is_staff:
            return RetrieveUpdateDestroyAPIView.patch(self, request, *args, **kwargs)
        return Response(status=401)
