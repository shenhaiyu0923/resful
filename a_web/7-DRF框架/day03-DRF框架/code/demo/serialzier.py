import serialziers
class BookSerialzier(serialziers.BaseSerialier):


    def validate(self, attrs):
        print('多个字段验证')
        return attrs

    def create(self, validate_data):
        print('保存数据')

    def update(self, instance, validate_data):

        print('更新数据')
