from rest_framework import serializers
from django.db.models import Sum
from transactions.models import Transaction
from categories.serializers import CategorySerializer
from .models import Budget

class BudgetSerializer(serializers.ModelSerializer):
    category_detail = CategorySerializer(source='category', read_only=True)
    spent = serializers.SerializerMethodField()
    remaining = serializers.SerializerMethodField()
    percent_used = serializers.SerializerMethodField()

    class Meta:
        model = Budget
        fields = [
            'id', 'category', 'category_detail',
            'limit_amount', 'month',
            'spent', 'remaining', 'percent_used',
        ]
        read_only_fields = ['id']

    def _get_spent(self, obj):
        result = Transaction.objects.filter(
            user=obj.user,
            category=obj.category,
            type='expense',
            date__year=obj.month.year,
            date__month=obj.month.month,
        ).aggregate(total=Sum('amount'))
        return result['total'] or 0
    

    def get_spent(self, obj):
        return self._get_spent(obj)


    def get_remaining(self, obj):
        return obj.limit_amount - self._get_spent(obj)


    def get_percent_used(self, obj):
        if obj.limit_amount == 0:
            return 0
        spent = self._get_spent(obj)
        return round((spent / obj.limit_amount) * 100, 1)


    def validate_month(self, value):
        return value.replace(day=1)


    def validate_limit_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError('Limit must be greater than zero')
        return value
  