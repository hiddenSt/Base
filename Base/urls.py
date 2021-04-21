from django.urls import path, include
from api import urls


urlpatterns = [
    path('', include('api.urls')),
    path('api/', include('authentication.urls'))
]
