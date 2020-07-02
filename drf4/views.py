from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView

from drf4.Serializer import  usere
from app.models import user
from drf4.SimpleRate import SendMessageRate
from drf4.authenticat import MyAuth
from utils.response import apiresponse


class twousernaes(viewsets.ModelViewSet):
    queryset = user.objects.filter(is_delete=False)
    serializer_class = usere
    lookup_field = "id"
    #登录逻辑
    def logint(self, request, *args, **kwargs):
        name = request.data
        nam = name["username"]
        pwd = name["password"]
        usernae = user.objects.filter(username=nam,password=pwd)
        if usernae :
            return apiresponse(200,"登陆成功")
        else:
            return apiresponse(400,"用户名或密码错误！")
    #注册逻辑
    def post(self,request, *args, **kwargs):
        self.create(request, *args, **kwargs)
        return apiresponse(200,"注册成功！")




class TestPermissionAPIView(APIView):
    authentication_classes = [MyAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return APIResponse("登录访问成功")




class UserLoginOrReadOnly(APIView):
    throttle_classes = [UserRateThrottle]

    def get(self, request, *args, **kwargs):
        return APIResponse("读操作访问成功")

    def post(self, request, *args, **kwargs):
        return APIResponse("写操作")


class SendMessageAPIView(APIView):
    throttle_classes = [SendMessageRate]

    def get(self, request, *args, **kwargs):
        return APIResponse("读操作访问成功")

    def post(self, request, *args, **kwargs):
        return APIResponse("写操作")
