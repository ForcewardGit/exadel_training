from django.urls import reverse
import pytest
from faker import Faker
from users.models import RegularUser, User


fake = Faker()
pytestmark = pytest.mark.django_db


class TestRegularUserEndpoints:
    url_1 = reverse("users-regular_users")
    url_2 = reverse("users-regular_user", args = [2])

    
    def test_list(self, api_client):
        response = api_client.get(self.url_1)

        assert response.status_code == 200
    
    
    def test_create(self, api_client, user_create):
        user = user_create
        new_regular_user_data = {
            "user": user.id,
            "name": fake.first_name(),
            "surname": fake.last_name()
        }

        response = api_client.post(self.url_1, data = new_regular_user_data, format = "json")
        wrong_regular_user_data = new_regular_user_data
        wrong_regular_user_data["surname"] = ""
        response_400 = api_client.post(self.url_1, data = wrong_regular_user_data)

        assert response.status_code == 201
        assert User.objects.filter(pk = response.data["user"]).exists()
        assert response_400.status_code == 400
    

    def test_detail(self, api_client, regular_user_create):
        regular_user = regular_user_create
        response = api_client.get(self.url_2)

        assert response.status_code == 200
        assert response.data["name"] == regular_user.name
    

    def test_update(self, api_client, regular_user_create):

        put_data_correct = {
            "user": regular_user_create.user.id,
            "name": fake.first_name(),
            "surname": fake.last_name()
        }

        url = reverse("users-regular_user", args=[regular_user_create.id])
        response = api_client.put(url, data = put_data_correct)
        regular_user = RegularUser.objects.get(user = put_data_correct["user"])

        assert response.status_code == 200
        assert regular_user is not None
        assert response.data["surname"] == regular_user.surname
    

    def test_delete(self, api_client, regular_user_create):
        regular_user = regular_user_create
        url = reverse("users-regular_user", args=[regular_user_create.id])

        response = api_client.delete(url)

        assert response.status_code == 204
        with pytest.raises(RegularUser.DoesNotExist):
            RegularUser.objects.get(id = regular_user.id)
