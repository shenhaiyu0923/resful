class BaseSerialier(object):
    """
        基础序列化器
    """

    def __init__(self, instance=None, data=None):
        self.instance = instance
        self._data = data

    def validate(self, attrs):
        """
            多个字段验证方法
        :param attrs:
        :return:
        """
        pass

    def is_valid(self):
        """
            验证
        :return:
        """
        data = self.validate(attrs=self.data)
        self._data = data

    def save(self):
        """
            保存更新方法
        :return:
        """


        if self.instance is not None:
            self.instance = self.update(instance=self.instance, validate_data=self.data)
        else:
            self.instance = self.create(validate_data=self.data)

    def update(self, instance, validate_data):
        pass

    def create(self, validate_data):
        pass


    @property
    def data(self):

        return {'btitle':'python'}
