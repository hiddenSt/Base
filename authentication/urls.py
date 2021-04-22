from django.urls import path

from .views import RegistrationAPIView, ObtainTokenAPIView

app_name = 'authentication'
urlpatterns = [
    path('users/', RegistrationAPIView.as_view(), name='register'),
    path('tokens/', ObtainTokenAPIView.as_view(), name='obtain_token'),
    path('tokens/', )
]
