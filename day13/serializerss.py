from rest_framework.serializers import ModelSerializer

from app.models import Book


class ComputerModelSerializer(ModelSerializer):
    class Meta:
        model = Book
        # 代表与模型所有字段进行映射
        # 大多数情况下都需要声明序列化去反序列化字段
        fields = ("book_name", "price")
