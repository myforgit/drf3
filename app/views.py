from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView,CreateAPIView
from app.Serializer import book
from app.models import Book

#增删改查的原代码
class usernaes(APIView):
    def get(self, request, *args, **kwargs):
        book_id = kwargs.get("id")
        if book_id:
            book_ser = Book.objects.get(id=book_id, is_delete=False)
            book_obj = book(book_ser).data
            return Response({
                "status": status.HTTP_200_OK,
                "mig": "查询单个用户成功！",
                "request": book_obj
            })
        else:
            book_ser = Book.objects.filter(is_delete=False)
            book_obj = book(book_ser, many=True).data
            return Response({
                "status": status.HTTP_200_OK,
                "mig": "查询所有用户成功！",
                "request": book_obj
            })

    def post(self, request, *args, **kwargs):
        book_id = request.data
        if isinstance(book_id, dict):
            many = False
        elif isinstance(book_id, list):
            many = True
        else:
            return Response({
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "mig": "添加数据有误",
            })
        book_ser = book(data=book_id, many=many)
        book_ser.is_valid(raise_exception=True)
        book_obj = book_ser.save()
        return Response({
            "status": status.HTTP_200_OK,
            "mig": "添加用户成功！",
            "request": book(book_obj, many=many).data
        })

    def delete(self, request, *args, **kwargs):
        book_id = kwargs.get("id")
        if book_id:
            book_ser = [book_id]
        else:
            book_ser = request.data.get("book_ser")
        book_obj = Book.objects.filter(pk__in=book_ser, is_delete=False).update(is_delete=True)
        if book_obj:
            return Response({
                "status": status.HTTP_200_OK,
                "mig": "删除用户成功！",
            })
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "message": "删除失败或图书不存在"
        })

    def patch(self, request, *args, **kwargs):
        request_data = request.data
        book_id = kwargs.get("id")
        try:
            book_obj = Book.objects.get(pk=book_id)
        except:
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "图书不存在"
            })
        book_ser = book(data=request_data, instance=book_obj, partial=True)
        book_ser.is_valid(raise_exception=True)
        book_ser.save()
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "message": "更新成功",
            "results": book(book_obj).data
        })

#对于增删改查的封装

class naes(RetrieveUpdateDestroyAPIView,CreateAPIView):
    queryset = Book.objects.filter(is_delete=False)
    serializer_class = book
    lookup_field = 'id'