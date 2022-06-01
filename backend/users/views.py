from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from .models import User, RegularUser, Company, Service
from .serializers import RegularUserSerializer, UserSerializer, CompanySerializer, ServiceSerializer


@api_view(["GET", "POST"])
def general_users(request):
    if request.method == 'POST':
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    all_users = User.objects.all()
    serializer = UserSerializer(all_users, many = True)
    return Response(serializer.data)


@api_view(["GET", "POST"])
def regular_users(request):
    if request.method == "POST":
        serializer = RegularUserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    all_users = RegularUser.objects.all()
    serializer = RegularUserSerializer(all_users, many = True)

    return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
def regular_user(request, pk):
    try:
        user = RegularUser.objects.get(id = pk)
        print(request.user.is_staff, user.user.is_staff)
    except RegularUser.DoesNotExist:
        return HttpResponse(status = 404)

    if request.method == "GET":
        serializer = RegularUserSerializer(user, many = False)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        if request.user.id == user.user.id or request.user.is_staff:
            serializer = RegularUserSerializer(user, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return JsonResponse(serializer.errors, status = 400)
        return HttpResponse(status=401)
    
    elif request.method == "DELETE":
        if (request.user.id == user.user.id or request.user.is_staff):
            user.delete()
            return HttpResponse(status = 204)
        return HttpResponse(status=401)



@api_view(["GET", "PUT", "DELETE"])
def user_details(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = UserSerializer(user, many = False)
        return Response(serializer.data)

    elif request.method == "PUT":
        if request.user.id == user.user.id or request.user.is_staff:
            data = JSONParser().parse(request)
            serializer = UserSerializer(user, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return JsonResponse(serializer.errors, status=400)
        return HttpResponse(status=401)

    elif request.method == 'DELETE':
        if request.user.id == user.user.id or request.user.is_staff:
            user.delete()
            return HttpResponse(status=204)
        return HttpResponse(status=401)


@api_view(["GET", "POST"])
def companies_list(request):
    if request.method == "GET":
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many = True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CompanySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
def company_details(request, name):
    # name = name.capitalize()
    try:   
        company = Company.objects.get(name = name)
    except Company.DoesNotExist:
        return HttpResponse(status = 404)
    
    if request.method == "GET":
        serializer = CompanySerializer(company, many = False)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        if request.user.id == company.user.id or request.user.is_staff:
            serializer = CompanySerializer(company, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return JsonResponse(serializer.errors, status = 400)
        return HttpResponse(status=401)
    
    elif request.method == "DELETE":
        if request.user.id == company.user.id or request.user.is_staff:
            company.delete()
            return HttpResponse(status=204)
        return HttpResponse(status=401)


### Service views ###
@api_view(["GET", "POST"])
def services_list(request):
    if request.method == "GET":
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many = True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ServiceSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
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
def service_companies(request, pk):
    service = Service.objects.get(id=pk)
    filtered_companies = Company.objects.filter(services__id = service.id)
    serializer = CompanySerializer(filtered_companies, many = True)

    return Response(serializer.data)
