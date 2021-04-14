from rest_framework import serializers


class RequestSerializer(serializers.Serializer):
    request_params = serializers.CharField(max_length=200)


    def validate(self, data):
        if not data['request_params']:
            raise serializers.ValidationError("Required")
        return data