from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

def google_auth_complete(request):
    user = request.user

    if not user .is_authenticated:
        return redirect('/login/?error=google_failed')
    
    refresh = RefreshToken.for_user(user)
    access = str(refresh.access_token)
    refresh_token = str(refresh)

    return redirect(f'/?access={access}&refresh={refresh_token}')
