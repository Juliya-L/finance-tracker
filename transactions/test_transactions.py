import pytest
from django.urls import reverse
from datetime import date

from .models import Transaction
from categories.models import Category


@pytest.fixture
def user_with_category(create_user):
    user = create_user()

    category = Category.objects.create(
        user=user,
        name='Food',
        type='expense'
    )

    return user, category


@pytest.mark.django_db
class TestTransactions:

    def test_create_transaction(self, api_client, user_with_category):
        user, category = user_with_category

        api_client.force_authenticate(user=user)

        url = reverse('transaction-list')

        data = {
            'amount': '150.00',
            'type': 'expense',
            'date': '2026-05-01',
            'note': 'Lunch',
            'category': category.pk,
        }

        response = api_client.post(url, data)

        assert response.status_code == 201
        assert Transaction.objects.filter(user=user).count() == 1

    def test_filter_by_type(self, api_client, user_with_category):
        user, category = user_with_category

        api_client.force_authenticate(user=user)

        Transaction.objects.create(
            user=user,
            category=category,
            amount=100,
            type='expense',
            date=date.today()
        )

        Transaction.objects.create(
            user=user,
            category=category,
            amount=500,
            type='income',
            date=date.today()
        )

        url = reverse('transaction-list')

        response = api_client.get(url, {'type': 'expense'})

        assert response.status_code == 200
        assert response.data['count'] == 1

    def test_cannot_see_others_transactions(
        self,
        api_client,
        create_user,
        user_with_category
    ):
        user, category = user_with_category

        other = create_user()

        Transaction.objects.create(
            user=user,
            category=category,
            amount=100,
            type='expense',
            date=date.today()
        )

        api_client.force_authenticate(user=other)

        url = reverse('transaction-list')

        response = api_client.get(url)

        assert response.status_code == 200
        assert response.data['count'] == 0

    def test_negative_amount_rejected(
        self,
        api_client,
        user_with_category
    ):
        user, category = user_with_category

        api_client.force_authenticate(user=user)

        url = reverse('transaction-list')

        data = {
            'amount': '-50.00',
            'type': 'expense',
            'date': '2026-05-01',
            'category': category.pk,
        }

        response = api_client.post(url, data)

        assert response.status_code == 400