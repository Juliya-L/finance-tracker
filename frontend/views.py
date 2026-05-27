from django.shortcuts import render, redirect
from django.views import View


class LoginView(View):
    def get(self, request):
        return render(request, 'frontend/login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'frontend/register.html')


class DashboardView(View):
    def get(self, request):
        return render(request, 'frontend/dashboard.html')


class TransactionsView(View):
    def get(self, request):
        return render(request, 'frontend/transactions.html')


class CategoriesView(View):
    def get(self, request):
        return render(request, 'frontend/categories.html')


class AnalyticsView(View):
    def get(self, request):
        return render(request, 'frontend/analytics.html')
    
class BudgetsView(View):
    def get(self, request):
        return render(request, 'frontend/budgets.html')