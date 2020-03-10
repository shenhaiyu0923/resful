from rest_framework import serializers


# 自定义序列化器
class BookSerialzier(serializers.Serializer):
    # 序列化返回字段
    btitle = serializers.CharField()
    bread = serializers.IntegerField()
    bpub_date = serializers.DateField()
