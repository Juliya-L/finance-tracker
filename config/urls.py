
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from users.social_auth import google_auth_complete

urlpatterns = [
    path('', include('frontend.urls')),
    path('auth/', include('social_django.urls', namespace='social')),
    path('auth/done/', google_auth_complete, name='google_done'),
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/categories/', include('categories.urls')),
    path('api/transactions/', include('transactions.urls')),
    path('api/analytics/', include('analytics.urls')),
    path('api/budgets/', include('budgets.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
       ]
