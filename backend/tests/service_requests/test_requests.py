import pytest
from faker import Faker
from django.urls import reverse
from users.models import *
from service_requests.models import Request


pytestmark = pytest.mark.django_db
fake = Faker()


class TestRequestEndpoints:
    def create_request(self):
        regular_user = RegularUser.objects.create(
            username = "test_username_1",
            password = "test_password_name",
            name = fake.first_name(),
            surname = fake.last_name()
        )
        company = Company.objects.create(
            username = "another_test_user",
            password = "test_password_name",
            name = "Exadel"
        )
        service = Service.objects.create(name = "Service Test")
        address = Address.objects.create(user_id = regular_user, country = "India", city = "Mumbai", street = "Some street road", house_number = 23, ap_number = 98)

        request = {
            "total_area": 188.5,
            "user": regular_user.id,
            "service": service.id,
            "company": company.id,
            "address": address.id
        }

        return request


    def test_list(self, api_client):
        url = reverse("requests")
        response = api_client.get(url)

        assert response.status_code == 200
    
    
    def test_create(self, api_client):
        request_1 = self.create_request()
        request_2 = request_1.copy()
        request_2["total_area"] = ""
        url = reverse("requests")

        response_1 = api_client.post(url, data = request_1)
        response_2 = api_client.post(url, data = request_2)

        assert response_1.status_code == 201
        assert Request.objects.count() == 1
        assert response_2.status_code == 400
    

    def test_detail(self, api_client):
        request_1 = self.create_request()
        request_object = Request.objects.create(
            total_area = request_1["total_area"],
            user = RegularUser.objects.get(pk = request_1["user"]),
            service = Service.objects.get(pk = request_1["service"]),
            company = Company.objects.get(pk = request_1["company"]),
            address = Address.objects.get(pk = request_1["address"])
        )
        url = reverse("request", args=[request_object.id])

        response = api_client.get(url)

        assert response.status_code == 200
        assert response.data["id"] == request_object.id
    

    def test_update(self, api_client):
        request_1 = self.create_request()
        request_object = Request.objects.create(
            total_area = request_1["total_area"],
            user = RegularUser.objects.get(pk = request_1["user"]),
            service = Service.objects.get(pk = request_1["service"]),
            company = Company.objects.get(pk = request_1["company"]),
            address = Address.objects.get(pk = request_1["address"])
        )

        url = reverse("request", args=[request_object.id])
        response_old = api_client.get(url)

        put_data = {
            "total_area": 198.5,
            "user": request_object.user.id,
            "service": request_object.service.id,
            "company": request_object.company.id,
            "address": request_object.address.id
        }

        response_new = api_client.put(url, data = put_data)

        assert response_new.status_code == 200
        assert response_new.data["user"] == response_old.data["user"]
        assert response_old.data["total_area"] != response_new.data["total_area"]

    
    def test_delete(self, api_client):
        request_1 = self.create_request()
        request_object = Request.objects.create(
            total_area = request_1["total_area"],
            user = RegularUser.objects.get(pk = request_1["user"]),
            service = Service.objects.get(pk = request_1["service"]),
            company = Company.objects.get(pk = request_1["company"]),
            address = Address.objects.get(pk = request_1["address"])
        )

        url = reverse("request", args=[request_object.id])
        response = api_client.delete(url)

        assert response.status_code == 204
        with pytest.raises(Request.DoesNotExist):
            Request.objects.get(id = request_object.id)
    

    def test_user_requests(self, api_client):
        request_1 = self.create_request()
        request_object = Request.objects.create(
            total_area = request_1["total_area"],
            user = RegularUser.objects.get(pk = request_1["user"]),
            service = Service.objects.get(pk = request_1["service"]),
            company = Company.objects.get(pk = request_1["company"]),
            address = Address.objects.get(pk = request_1["address"])
        )

        url = reverse("user_requests", args=[request_object.user.user.username])
        response = api_client.get(url)

        assert response.status_code == 200
