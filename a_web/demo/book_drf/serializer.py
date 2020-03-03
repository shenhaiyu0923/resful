from rest_framework import serializers


class BookSerializer(serializers.Serializer):
    # 序列化返回字段
    btitle = serializers.CharField()
    bread = serializers.IntegerField()
    bpub_date = serializers.DateField()