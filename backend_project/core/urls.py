from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import public_view, protected_view, secret_view, RegisterUserView, trigger_email
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('hello/', public_view),
    path('secret/', secret_view, name='secret'),
    path('login/', obtain_auth_token, name='api_token_auth'),  

    # JWT token routes
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('register/', RegisterUserView.as_view(), name='register'),
    path('send-email/', trigger_email),
]
