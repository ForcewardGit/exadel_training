from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from .models import User, RegularUser, Company, Service
from .serializers import RegularUserSerializer, UserSerializer, UserRegisterSerializer, CompanySerializer, ServiceSerializer
from .permissions import GeneralUserPermission, RegularUserPermission, CompanyPermission
from .tasks import print_message_to_terminal


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated | IsAdminUser])
def general_users(request):
    if request.method == 'POST':
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return HttpResponse(status = 400)
    
    elif request.method == "GET":
        all_users = User.objects.all()
        serializer = UserSerializer(all_users, many = True)
        return Response(serializer.data)


@api_view(["POST"])
def register_user(request):
    if request.method == "POST":
        serializer = UserRegisterSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            print_message_to_terminal.delay()
            return Response({
                "user": UserSerializer(user).data,
                "message": "User was created successfully! To login -> get token."
            }, status = 201)
        return HttpResponse(status = 400)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def regular_users(request):
    if request.method == "POST":
        serializer = RegularUserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return HttpResponse(status = 400)

    elif request.method == "GET":
        all_users = RegularUser.objects.all()
        serializer = RegularUserSerializer(all_users, many = True)
        return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated & (IsAdminUser | RegularUserPermission)])
def regular_user(request, pk):
    try:
        user = RegularUser.objects.get(id = pk)
    except RegularUser.DoesNotExist:
        return HttpResponse(status = 404)

    if request.method == "GET":
        serializer = RegularUserSerializer(user, many = False)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        if request.user.is_staff or request.user.id == user.user.id:
            serializer = RegularUserSerializer(user, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = 200)
            return JsonResponse(serializer.errors, status = 400)
        return HttpResponse(status=401)

    elif request.method == "DELETE":
        if request.user.is_staff or request.user.id == user.user.id:
            user.delete()
            return HttpResponse(status = 204)
        return HttpResponse(status=401)
       

@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated, IsAdminUser | GeneralUserPermission])
def user_details(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = UserSerializer(user, many = False)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)
        

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def companies_list(request):
    if request.method == "GET":
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many = True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CompanySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return HttpResponse(status = 400)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly, IsAdminUser | CompanyPermission])
def company_details(request, name):
    try:
        company = Company.objects.get(name = name)
    except Company.DoesNotExist:
        return HttpResponse(status = 404)
    
    if request.method == "GET":
        serializer = CompanySerializer(company, many = False)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        if request.user.is_staff or request.user.id == company.user.id:
            serializer = CompanySerializer(company, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = 200)
            return JsonResponse(serializer.errors, status = 400)
        return HttpResponse(status=401)
    
    elif request.method == "DELETE":
        if request.user.is_staff or request.user.id == company.user.id: 
            company.delete()
            return HttpResponse(status=204)
        return HttpResponse(status=401)


### Service views ###
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def services_list(request):
    if request.method == "GET":
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many = True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ServiceSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=201)
        return HttpResponse(status=400)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly])
def service_detail(request, pk):
    try:   
        service = Service.objects.get(id = pk)
    except Service.DoesNotExist:
        return HttpResponse(status = 404)
    
    if request.method == "GET":
        serializer = ServiceSerializer(service, many = False)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        if request.user.is_staff:
            serializer = ServiceSerializer(service, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return JsonResponse(serializer.errors, status = 400)
        return HttpResponse(status=401)
    
    elif request.method == "DELETE":
        if request.user.is_staff:
            service.delete()
            return HttpResponse(status=204)
        return HttpResponse(status=401)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def service_companies(request, pk):
    service = Service.objects.get(id=pk)
    filtered_companies = Company.objects.filter(services__id = service.id)
    serializer = CompanySerializer(filtered_companies, many = True)

    return Response(serializer.data)
