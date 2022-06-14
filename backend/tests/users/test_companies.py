from django.urls import reverse
import pytest
from faker import Faker
from users.models import Company


fake = Faker()
pytestmark = pytest.mark.django_db


class TestCompanyEndpoints:
    url_1 = reverse("users-companies")

    
    def test_list(self, api_client):
        response = api_client.get(self.url_1)

        assert response.status_code == 200
    
    
    def test_create(self, api_client, company_create):
        new_company_data = {
            "username": "another_company_owner",
            "password": company_create.password,
            "name": "Testcomp-Ltd"
        }

        response = api_client.post(self.url_1, data = new_company_data)

        assert response.status_code == 201
        assert Company.objects.filter(username = response.data["username"]).exists()
    

    def test_detail(self, api_client, company_create):
        company = company_create
        url = reverse("users-company_details", args = [company.name])
        response = api_client.get(url)

        assert response.status_code == 200
        assert response.data["name"] == company.name
    

    def test_update(self, api_client, company_create):

        put_data_correct = {
            "username": company_create.username,
            "password": company_create.password,
            "name": "Test-Ltd",
        }

        url = reverse("users-company_details", args=[company_create.name])
        response = api_client.put(url, data = put_data_correct)
        company = Company.objects.get(username = put_data_correct["username"])

        assert response.status_code == 200
        assert company is not None
        assert response.data["name"] == put_data_correct["name"]
    

    def test_delete(self, api_client, company_create):
        company = company_create
        url = reverse("users-company_details", args=[company.name])

        response = api_client.delete(url)

        assert response.status_code == 204
        with pytest.raises(Company.DoesNotExist):
            Company.objects.get(id = company.id)
