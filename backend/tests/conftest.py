import pytest
from users.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


client = APIClient()

@pytest.fixture
def api_client():
    username = 'test_username'
    password = 'test_user_password'
    user = User.objects.create_user(username=username, password=password)
    user.is_staff = True
    user.save()

    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    return client
