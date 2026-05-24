import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
class TestRegister:
    def test_register_success(self, api_client):
        url = reverse('register')
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpass123',
            'password2': 'testpass123',
        }  
        response = api_client.post(url, data)

        assert response.status_code == 201
        assert 'access' in response.data
        assert 'refresh' in response.data
        assert User.objects.filter(email='test@example.com').exists()
      

    def test_register_password_dont_match(self, api_client):
        url = reverse('register')
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpass123',
            'password2': 'wrongpass123',
        }

        response = api_client.post(url, data)

        assert response.status_code == 400

    def test_register_duplicate_email(self, api_client, create_user):
        create_user(email ='exists@example.com')
        url = reverse('register')
        data = {
            'username': 'newuser',
            'email': 'exists@example.com',
            'password': 'testpass123',
            'password2': 'testpass123',
        }
        response = api_client.post(url, data)

        assert response.status_code == 400


@pytest.mark.django_db
class TestProfile:
    def test_get_profile(self, auth_client):
        client, user = auth_client
        url = reverse('profile')
        response = client.get(url)

        assert response.status_code == 200
        assert response.data['email'] == user.email

    def test_profile_unauthorized(self, api_client):
        url = reverse('profile')
        response = api_client.get(url)

        assert response.status_code == 401

    def test_update_profile(self, auth_client):
        client, user = auth_client
        url = reverse('profile')
        response = client.patch(url, {'currency': 'USD'})

        assert response.status_code == 200
        assert response.data['currency'] == 'USD'

