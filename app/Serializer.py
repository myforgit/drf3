from rest_framework import serializers, exceptions

from app.models import Book



class book(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields =("book_name", "price", "publish", "authors", "pic")

        extra_kwargs={
            "book_name": {
                "required": True,  # 设置为必填字段
                "min_length": 3,  # 最小长度
                "error_messages": {
                    "required": "图书名是必填的",
                    "min_length": "长度不够，太短啦~"
                }
            },
            # 指定此字段只参与反序列化
            "publish": {
                "write_only": True
            },
            "authors": {
                "write_only": True
            },
            # 指定某个字段只参与序列化
            "pic": {
                "read_only": True
            }
        }

        def validate_book_name(self, value):
            # 自定义用户名校验规则
            if "1" in value:
                raise exceptions.ValidationError("图书名含有敏感字")
            return value

        # 全局校验钩子  可以通过attrs获取到前台发送的所有的参数
        def validate(self, attrs):

            price = attrs.get("price", 0)
            # 没有获取到 price  所以是 NoneType
            if price > 90:
                raise exceptions.ValidationError("超过设定的最高价钱~")

            return attrs


