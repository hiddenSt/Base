import json

from rest_framework.renderers import JSONRenderer


class UserJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        access_token = data.get('access_token', None)
        refresh_token = data.get('refresh_token', None)

        if access_token is not None and isinstance(access_token, bytes):
            data['access_token'] = access_token.decode('utf-8')

        if refresh_token is not None and isinstance(refresh_token, bytes):
            data['refresh_token'] = refresh_token.decode('utf-8')

        return json.dumps({
            'user': data
        })
