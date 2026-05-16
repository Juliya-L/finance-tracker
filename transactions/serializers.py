from rest_framework import serializers
from .models import Transaction
from categories.serializers import CategorySerializer

class TransactionSerializer(serializers.ModelSerializer):
    category_detail = CategorySerializer(source = 'category', read_only=True)

    class Meta:
        model = Transaction
        fields = [
            'id', 'amount', 'type', 'date', 'note',
            'category',
            'category_detail',
            'created_at',
        ]

        read_only_fields = ['id', 'created_at']

    def validate_amount(self, value):
        if value <=0:
            raise serializers.ValidationError('The sum must be greater than zero')
        return value
    