import pytest
from django.urls import reverse
from users.models import User
from rest_framework.test import APIClient



pytestmark = pytest.mark.django_db


class TestGeneralUserEndpoints:
    url_1 = reverse('general_users')
    url_2 = reverse("general_users-detail", args = ["new_user"])


    def test_list(self, api_client):
        response = api_client.get(self.url_1)

        assert response.status_code == 200


    def test_create(self, api_client):
        new_user = {
            "username": "new_user",
            "password": "user_new_password_1234"
        }

        response = api_client.post(self.url_1, data = new_user)

        assert response.status_code == 201
        assert User.objects.filter(username = new_user["username"]).exists()
    
    
    def test_detail(self, api_client, user_create):
        user = user_create
        response = api_client.get(self.url_2)

        assert response.status_code == 200
        assert response.data["username"] == user.username

    
    def test_update(self, api_client, user_create):
        user = user_create

        put_data_correct = {
            "password": user.password,
            "username": user.username,
            "email": "example@gmail.com"
        }
        put_data_incorrect = {
            "username": user.username,
            "email": "example@gmail.com"
        }
        
        response_1 = api_client.put(self.url_2, put_data_correct, format = "json")
        response_2 = api_client.put(self.url_2, data = put_data_incorrect)

        assert response_1.status_code == 200
        assert User.objects.get(username = user.username).email == put_data_correct["email"]
        assert response_2.status_code == 400


    def test_delete(self, api_client, user_create):
        user = user_create

        response = api_client.delete(self.url_2)

        assert response.status_code == 204
        with pytest.raises(User.DoesNotExist):
            User.objects.get(username = user.username)
