class GenericAPIView(object):
    queryset = None
    serializer_class = None

    def get_queryset(self):
        """
            获取去所有查询集
        :return:
        """
        return self.queryset

    def get_object(self):
        """
            获取查询集中的单一数据
        :return:
        """


        for instanse in self.queryset:
            if instanse.id == 1:
                return instanse

    def get_serializer(self,data=None):
        # 获取呀指定序列化器对象

        serializer = self.get_serializer_class()
        return serializer(data=data)

    def get_serializer_class(self):
        # 返回序列化器

        return self.serializer_class
