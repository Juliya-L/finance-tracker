from django.urls import path
from .views import SummaryView, ByCategoryView, MonthlyTrendView, BalanceView

urlpatterns = [
    path('summary/', SummaryView.as_view(), name='analytics-summary'),
    path('by-category/', ByCategoryView.as_view(), name='analytics-by-category'),
    path('monthly-trend/', MonthlyTrendView.as_view(), name='analytics-monthly-trend'),
    path('balance/', BalanceView.as_view(), name='analytics-balance'),
]