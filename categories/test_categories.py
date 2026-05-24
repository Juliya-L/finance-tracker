import pytest
from django.urls import reverse
from .models import Category


@pytest.mark.django_db
class TestCategories:

    def test_create_category(self, auth_client):
        client, user = auth_client
        url = reverse('category-list')
        data = {
            'name': 'Cafe',
            'type': 'expense',
            'icon': 'coffee',
            'color': '#f59e0b',
        }
        response = client.post(url, data)

        assert response.status_code == 201
        assert response.data['name'] == 'Cafe'
        assert Category.objects.filter(user=user, name='Cafe').exists()

    def test_list_only_own_categories(self, api_client, create_user):
        user1 = create_user()
        user2 = create_user()

        Category.objects.create(user=user1, name='My category', type='expense')
        Category.objects.create(user=user2, name='Other category', type='expense')

        api_client.force_authenticate(user=user1)
        url = reverse('category-list')
        response = api_client.get(url)

        assert response.status_code == 200
        assert response.data['count'] == 1
        assert response.data['results'][0]['name'] == 'My category'

    def test_delete_category(self, auth_client):

        client, user = auth_client
        category = Category.objects.create(user=user, name='Test', type='expense')

        url = reverse('category-detail', kwargs={'pk': category.pk})
        response = client.delete(url)

        assert response.status_code == 204
        assert not Category.objects.filter(pk=category.pk).exists()

    def test_cannot_delete_others_category(self, api_client, create_user):
       
        owner = create_user()
        other = create_user()
        category = Category.objects.create(user=owner, name='Other', type='expense')

        api_client.force_authenticate(user=other)
        url = reverse('category-detail', kwargs={'pk': category.pk})
        response = api_client.delete(url)

        assert response.status_code == 404