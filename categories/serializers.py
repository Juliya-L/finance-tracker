from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'type', 'icon', 'color']

    def validate_name(self, value):
        request = self.context.get('request')
        if not request:
            return value

      
        qs = Category.objects.filter(user=request.user, name=value)

       
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise serializers.ValidationError(
                f'You already have a category named "{value}"'
            )
        return value