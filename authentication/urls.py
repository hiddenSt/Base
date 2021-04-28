from django.urls import path

from .views import RegistrationAPIView, ObtainTokenAPIView, RefreshTokenAPIView

app_name = 'authentication'
urlpatterns = [
    path('users/', RegistrationAPIView.as_view(), name='register'),
    path('tokens/', ObtainTokenAPIView.as_view(), name='obtain_token'),
    path('tokens/refresh', RefreshTokenAPIView.as_view(), name='refresh_token')
]
