from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Request
from .serializers import RequestSerializer
from users.models import RegularUser



### With Class-Based Views ###
class RequestsList(APIView):
    def get(self, request, format=None):
        if request.user.is_staff:
            requests = Request.objects.all()
            serializer = RequestSerializer(requests, many = True)
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
            
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
        r = self.get_object(pk) # request object with id = pk
        if request.user.is_staff or request.user.id == r.user.user.id:
            serializer = RequestSerializer(r)
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request, pk, format=None):
        r = self.get_object(pk)
        if request.user.is_staff or request.user.id == r.user.user.id:
            serializer = RequestSerializer(r, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, pk, format=None):
        r = self.get_object(pk) # request object with id = pk
        
        if request.user.is_staff or request.user.id == r.user.user.id:
            r.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_401_UNAUTHORIZED)


### With Functional views ###
@api_view(["POST"])
def create_request(request):
    serializer = RequestSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def request_detail(request, pk):
    r = Request.objects.get(id = pk) # request object with id = pk

    if request.method == "GET":
        if request.user.is_staff or request.user.id == r.user.user.id:
            serializer = RequestSerializer(r, many = False)
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    elif request.method == "DELETE":
        if request.user.is_staff or request.user.id == r.user.user.id:
            r.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    elif request.method == "PUT":
        if request.user.is_staff or request.user.id == r.user.user.id:            
            serializer = RequestSerializer(r, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(["GET"])
def user_requests(request, username):
    if request.user.username == username or request.user.is_staff:
        user = RegularUser.objects.get(user__username = username)
        requests = Request.objects.filter(user = user)
        serializer = RequestSerializer(requests, many = True)

        return Response(serializer.data)

    return Response(status=status.HTTP_401_UNAUTHORIZED)