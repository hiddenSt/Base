from rest_framework import serializers
from Base.models import RequestModel


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestModel
        fields = ['timestamp', 'text', 'user']
