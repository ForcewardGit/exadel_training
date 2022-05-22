from django.http import Http404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import StaticHTMLRenderer

from .models import Request
from .serializers import RequestSerializer
from users.models import User, RegularUser



### With Viewsets ###
class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    @action(detail=False, renderer_classes=[StaticHTMLRenderer])
    def user_requests(self, request, *args, **kwargs):
        try:
            general_user = User.objects.get(username=kwargs["username"])
        except User.DoesNotExist:
            raise Http404
        user = RegularUser.objects.get(user = general_user)
        requests = Request.objects.filter(user = user)
        serializer = RequestSerializer(requests, many = True)

        return Response(serializer.data)



###############################################################################################################


### With Class-Based Views ###
class RequestsList(APIView):
    def get(self, request, format=None):
        requests = Request.objects.all()
        serializer = RequestSerializer(requests, many = True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = RequestSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)       


class RequestDetail(APIView):
    def get_object(self, pk):
        try:
            return Request.objects.get(id=pk)
        except Request.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        r = self.get_object(pk)
        serializer = RequestSerializer(r)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        r = self.get_object(pk)
        serializer = RequestSerializer(r, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        r = self.get_object(pk)
        r.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



###############################################################################################################


### With Function Views ###

@api_view(["GET", "POST"])
def all_requests(request):
    if request.method == "GET":
        requests = Request.objects.all()
        serializer = RequestSerializer(requests, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RequestSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(["GET", "PUT", ""])
def request_detail(request, pk):
    r = Request.objects.get(id = pk)
    serializer = RequestSerializer(r, many = False)

    return Response(serializer.data)


@api_view(["GET"])
def user_requests(request, username):
    try:
        general_user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404
    user = RegularUser.objects.get(user = general_user)
    requests = Request.objects.filter(user = user)
    serializer = RequestSerializer(requests, many = True)

    return Response(serializer.data)
