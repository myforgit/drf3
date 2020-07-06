from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from day12.Serializer import UserModelSerializer
from day12.togen import JWTAuthentication
from utils.response import Apiresponse
from rest_framework.views import APIView


# Create your views here.

class Usenname(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, *args, **kwargs):
        return Apiresponse(results={"username": request.user.username})


class Login(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        user_ser = UserModelSerializer(data=request.data)
        user_ser.is_valid(raise_exception=True)

        return Apiresponse(data_message="ok", token=user_ser.token, results=UserModelSerializer(user_ser.obj).data)
