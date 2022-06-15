from users.models import Service
from django.urls import reverse
import pytest
from faker import Faker


pytestmark = pytest.mark.django_db
fake = Faker()


class TestServices:
    def test_list(self, api_client):
        url = reverse("services")
        response = api_client.get(url)

        assert response.status_code == 200
    

    def test_create(self, api_client):
        url = reverse("services")

        service_1 = {"name": "Service 1"}
        service_2 = {"avg_price": 9}

        response_1 = api_client.post(url, data = service_1)
        response_2 = api_client.post(url, data = service_2)

        assert response_1.status_code == 201
        assert response_2.status_code == 400
        assert Service.objects.filter(name = service_1["name"]).exists()
    

    def test_detail(self, api_client, service_create):
        service = service_create
        url = reverse("service_detail", args = [service.id])
        response = api_client.get(url)

        assert response.status_code == 200
        assert response.data["name"] == service.name


    def test_update(self, api_client, service_create):
        url = reverse("service_detail", args=[service_create.id])
        response_old = api_client.get(url)

        put_data = {
            "name": fake.text(max_nb_chars = 30),
            "avg_price": 10
        }

        response_new = api_client.put(url, data = put_data)
        service = Service.objects.get(name = put_data["name"])

        assert response_new.status_code == 200
        assert service is not None
        assert response_new.data["name"] == service.name
        assert response_old.data["name"] != response_new.data["name"]
    

    def test_delete(self, api_client, service_create):
        service = service_create
        url = reverse("service_detail", args=[service.id])

        response = api_client.delete(url)

        assert response.status_code == 204
        with pytest.raises(Service.DoesNotExist):
            Service.objects.get(id = service.id)
    

    def test_service_companies(self, api_client, service_create):
        service = service_create
        url = reverse("service_companies", args=[service.id])

        response = api_client.get(url)

        assert response.status_code == 200
        