from rest_framework import serializers
from Base.models.request_model import Request


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['time', 'text', 'user']
