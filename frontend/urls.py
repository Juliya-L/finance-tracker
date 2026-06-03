from django.urls import path
from .views import (
    LoginView, RegisterView, DashboardView,
    TransactionsView, CategoriesView, AnalyticsView, BudgetsView, ForgotPasswordPageView, ResetPasswordPageView
)

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('transactions/', TransactionsView.as_view(), name='transactions'),
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('analytics/', AnalyticsView.as_view(), name='analytics'),
    path('budgets/', BudgetsView.as_view(), name='budgets'),
    path('forgot-password/', ForgotPasswordPageView.as_view(), name='forgot_password_page'),
    path('reset-password/', ResetPasswordPageView.as_view(), name='reset_password_page'),
]
