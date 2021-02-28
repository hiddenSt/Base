from rest_framework import serializers
from Base.models.request_model import RequestModel


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestModel
        fields = ['time', 'text', 'user']

