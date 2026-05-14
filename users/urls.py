from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, LogoutView, ProfileView, ChangePasswordView

urlpatterns = [
  path('register/', RegisterView.as_view(), name='register'),
  path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('logout/', LogoutView.as_view(), name='logout'), 
  path('me/', ProfileView.as_view(), name='profile'),
  path('change-password/', ChangePasswordView.as_view(), name='change_password'),

]
