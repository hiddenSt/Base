from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response


class RegisterView(APIView):
    def post(self, request: Request) -> Response:

        # Creates new user and generates JWT Token

        return  Response()
