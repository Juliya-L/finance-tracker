from django.urls import path
from .views import (
    LoginView, RegisterView, DashboardView,
    TransactionsView, CategoriesView, AnalyticsView, BudgetsView
)

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('transactions/', TransactionsView.as_view(), name='transactions'),
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('analytics/', AnalyticsView.as_view(), name='analytics'),
    path('budgets/', BudgetsView.as_view(), name='budgets'),
]
