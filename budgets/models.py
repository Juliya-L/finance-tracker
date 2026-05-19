from django.db import models
from django.conf import settings
from categories.models import Category

class Budget(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='budgets')
    category = models.ForeignKey(Category, on_delete= models.CASCADE, related_name='budgets')
    limit_amount = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.DateField()
    class Meta:
        ordering = ['-month']
        unique_together = ['user', 'category', 'month']


    def __str__(self):
        return f'{self.user.email} - {self.category.name} {self.month:%Y-%m}'