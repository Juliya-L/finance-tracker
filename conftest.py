import pytest
from faker import Faker
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()
fake = Faker('uk_UA')


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_user():
    def make_user(**kwargs):
        defaults = {
           'username': fake.user_name(),
           'email': fake.email(),
           'password': 'testpass123',
        }
        defaults.update(kwargs)
        return User.objects.create_user(**defaults)
    return make_user


@pytest.fixture
def auth_client(api_client, create_user):
    user = create_user()
    api_client.force_authenticate(user=user)
    return api_client, user

