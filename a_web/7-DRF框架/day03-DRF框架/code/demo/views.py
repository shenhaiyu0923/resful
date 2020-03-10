from generic import GenericAPIView
from serialzier import BookSerialzier

class BookView(GenericAPIView):
    queryset = [{'btitle':'1111','id':1},{'btitle':'2222','id':2}]
    serializer_class = BookSerialzier
    def post(self,request):

        #1、获取数据
        data=request
        # 验证数据
        ser=self.get_serializer(data=data)
        ser.is_valid()
        # 保存数据
        ser.save()
        # 返回结果
        return ser.data

request='python'
BookView().post(request)







