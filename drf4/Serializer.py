from rest_framework import serializers, exceptions

from app.models import Book, user


class usere(serializers.ModelSerializer):
    class Meta:
        model = user
        fields =("username","password")

        extra_kwargs={
            "book_name": {
                "required": True,  # 设置为必填字段
                "min_length": 1,  # 最小长度
                "error_messages": {
                    "required": "用户名是必填的",
                    "min_length": "长度不够，太短啦~"
                }
            },
            # 指定此字段只参与反序列化
            "username": {
                "write_only": True
            },
            "passwor": {
                "write_only": True
            },
        }

        def validate_book_name(self, value):
            # 自定义用户名校验规则
            if "1" in value:
                raise exceptions.ValidationError("图书名含有敏感字")
            return value



