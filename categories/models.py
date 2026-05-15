from django.db import models
from django.conf import settings

class Category(models.Model):
    INCOME = 'income'
    EXPENSE = 'expense'

    TYPE_CHOICES = [
        (INCOME, 'Income'),
        (EXPENSE, 'Expense'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='categories'
    )

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default=EXPENSE)
    icon = models.CharField(max_length=50, default='tag')
    color = models.CharField(max_length=7, default='#6366f1')

    class Meta:
        ordering = ['name']
        unique_together = ['user', 'name']

    def __str__(self):
        return f'{self.user.email} - {self.name}'
