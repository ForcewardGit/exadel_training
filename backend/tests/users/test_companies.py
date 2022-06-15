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
    
    
    def test_create(self, api_client, user_create):
        user = user_create
        new_company_data = {
            "user": user.id,
            "name": fake.text(max_nb_chars = 30)
        }

        response = api_client.post(self.url_1, data = new_company_data)

        assert response.status_code == 201
        assert Company.objects.filter(user = response.data["user"]).exists()
    

    def test_detail(self, api_client, company_create):
        company = company_create
        url = reverse("users-company_details", args = [company.name])
        response = api_client.get(url)

        assert response.status_code == 200
        assert response.data["name"] == company.name
    

    def test_update(self, api_client, company_create):

        put_data_correct = {
            "user": company_create.user.id,
            "name": fake.text(max_nb_chars = 30)
        }

        url = reverse("users-company_details", args=[company_create.name])
        response = api_client.put(url, data = put_data_correct)
        company = Company.objects.get(name = put_data_correct["name"])

        assert response.status_code == 200
        assert company is not None
        assert response.data["name"] == company.name
    

    def test_delete(self, api_client, company_create):
        company = company_create
        url = reverse("users-company_details", args=[company.name])

        response = api_client.delete(url)

        assert response.status_code == 204
        with pytest.raises(Company.DoesNotExist):
            Company.objects.get(id = company.id)
