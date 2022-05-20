from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Request
from .serializers import RequestSerializer
from users.models import User, RegularUser



### CRUD for Request ###
@api_view(["POST"])
def create_request(request):
    serializer = RequestSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)


@api_view(["POST"])
def update_request(request, pk):
    r = Request.objects.get(id=pk)
    serializer = RequestSerializer(data = request.data, instance = r)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)


@api_view(["POST"])
def delete_request(request, pk):
    r = Request.objects.get(id=pk)
    r.delete()

    return Response(f"Request was deleted successfully!")

# ========================================================== #


@api_view(["GET"])
def all_requests(request):
    requests = Request.objects.all()
    serializer = RequestSerializer(requests, many = True)

    return Response(serializer.data)


@api_view(["GET"])
def request_detail(request, pk):
    r = Request.objects.get(id = pk)
    serializer = RequestSerializer(r, many = False)

    return Response(serializer.data)


@api_view(["GET"])
def user_requests(request, username):
    general_user = User.objects.get(username = username)
    user = RegularUser.objects.get(user = general_user)
    requests = Request.objects.filter(user = user)
    serializer = RequestSerializer(requests, many = True)

    return Response(serializer.data)
