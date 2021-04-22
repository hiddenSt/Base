from datetime import datetime

from django.conf import settings
from rest_framework import authentication
from rest_framework import exceptions

import jwt

from .models import User




class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('Authorization')
        if not token:
            return None

        payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')

        if payload['exp'] < datetime.now():
            raise exceptions.AuthenticationFailed('Token expired')

        try:
            user = User.objects.get(id=payload.get('id'))
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return user, None
