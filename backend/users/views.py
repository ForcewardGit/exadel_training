from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User, RegularUser, Company, Service
from .serializers import CompanySerializer, ServiceSerializer, UserSerializer, RegularUserSerializer


@api_view(["GET"])
def general_users(request):
    all_users = User.objects.all()
    serializer = UserSerializer(all_users, many = True)

    return Response(serializer.data)


@api_view(["GET"])
def regular_users(request):
    all_users = RegularUser.objects.all()
    serializer = RegularUserSerializer(all_users, many = True)

    return Response(serializer.data)


@api_view(["GET"])
def regular_user(request, pk):
    user = RegularUser.objects.get(id = pk)
    serializer = RegularUserSerializer(user, many = False)

    return Response(serializer.data)


@api_view(["GET"])
def user_details(request, username):
    user = User.objects.get(username = username)
    serializer = UserSerializer(user, many = False)

    return Response(serializer.data)


@api_view(["GET"])
def companies_list(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many = True)

    return Response(serializer.data)


@api_view(["GET"])
def company_details(request, name):
    name = name.capitalize()
    company = Company.objects.get(name = name)
    serializer = CompanySerializer(company, many = False)

    return Response(serializer.data)


@api_view(["POST"])
def create_company(request):
    serializer = CompanySerializer(data = request.data)
    request.data["name"] = request.data["name"].capitalize()
    
    if serializer.is_valid():
        serializer.save()
     
    return Response(serializer.data)


@api_view(["POST"])
def update_company(request, name):
    name = name.capitalize()
    company = Company.objects.get(name = name)
    serializer = CompanySerializer(data = request.data, instance = company)

    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)


@api_view(["POST"])
def delete_company(request, name):
    name = name.capitalize()
    company = Company.objects.get(name = name)
    company.delete()

    return Response("Company was deleted successfully!")


### Service views ###
@api_view(["GET"])
def services_list(request):
    services = Service.objects.all()
    serializer = ServiceSerializer(services, many = True)

    return Response(serializer.data)


@api_view(["GET"])
def service_detail(request, pk):
    service = Service.objects.get(id=pk)
    serializer = ServiceSerializer(service, many = False)

    return Response(serializer.data)


@api_view(["POST"])
def create_service(request):
    serializer = ServiceSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)


@api_view(["POST"])
def update_service(request, pk):
    service = Service.objects.get(id=pk)
    serializer = ServiceSerializer(data = request.data, instance = service)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)


@api_view(["POST"])
def delete_service(request, pk):
    service = Service.objects.get(id=pk)
    service.delete()

    return Response(f"The service was deleted successfully!")


@api_view(["POST"])
def service_companies(request, pk):
    service = Service.objects.get(id=pk)
    filtered_companies = Company.objects.filter(services__id = service.id)
    serializer = CompanySerializer(filtered_companies, many = True)

    return Response(serializer.data)