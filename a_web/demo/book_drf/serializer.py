from rest_framework import serializers
from books.models import BookInfo
from django.db.transaction import atomic


class HeroInfoSerialzier(serializers.Serializer):
    # 英雄序列化器
    hname = serializers.CharField()
    hcomment = serializers.CharField()
    #hbook=serializers.PrimaryKeyRelatedField(read_only=True)
    hbook = serializers.StringRelatedField()

class BookSerializer(serializers.Serializer):
    # 序列化返回字段
    id = serializers.IntegerField(read_only=True)
    btitle = serializers.CharField(max_length=20, min_length=2,help_text='书名')
    bread = serializers.IntegerField(max_value=100, min_value=2)
    # btitle = serializers.CharField(max_length=20, min_length=5, write_only=False)
    # bread = serializers.IntegerField(max_value=100, min_value=5,read_only=False)
    bpub_date = serializers.DateField()
    bcomment = serializers.IntegerField(default=10)

    # 返回关联的英雄id   PrimaryKeyRelatedField
    # heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True,many=True)
    # 返回关联英雄模型类的str方法值
    # heroinfo_set = serializers.StringRelatedField(read_only=True, many=True)
    #heroinfo_set = HeroInfoSerialzier(many=True)

    # 单一字段验证validate_ + 字段名
    def validate_btitle(self, value):

        if value == 'python':
            raise serializers.ValidationError('书名不能是python')
        return value

    # 多个字段验证
    def validate(self, attrs):
        if attrs['bread'] < attrs['bcomment']:
            raise serializers.ValidationError('阅读量不能大于评论量')

        return attrs

    def create(self, validated_data):
        # 保存数据
        book = BookInfo.objects.create(**validated_data)# **validated_data 字典拆包处理

        return book

    def update(self, instance, validated_data):
        # 更新数据
        instance.btitle = validated_data['btitle']
        instance.bread = validated_data['bread']
        instance.save()
        return instance


class BookModelSerialzier(serializers.ModelSerializer):
    # 显示指明字段
    bread=serializers.IntegerField(max_value=100,min_value=20)
    sms_code=serializers.CharField(max_length=6,min_length=6)
    class Meta:
        model=BookInfo # 指定生成字段的模型类
        fields=('btitle','bread','sms_code') # 指定模型类中的字段
        # fields='__all__' # 指定模型类中的字段
        read_only_fields=('btitle',)
        # exclude=('btitle',)#取反操作
        # 添加修改字段选项参数
        # extra_kwargs={
        #     "bcomment":{
        #         'max_value':100
        #     },
        #     'btitle':{
        #         'min_length':5
        #     }
        #
        # }


    # def validate(self, attrs):

    # def validate_btitle(self, data):

# from book_drf.serializer import BookModelSerialzier
# BookModelSerialzier()