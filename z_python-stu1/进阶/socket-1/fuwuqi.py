#导入socket库
from socket import *
#主机地址为空字符串表示,所有的地址都绑定
#包括环回地址,所有的网络接口的ip地址127.0.0.1
#客户端必须
HOST = '0.0.0.0'
PORT = 21567
BUFSIZ=1024
ADDR = (HOST,PORT)

#创建socket,指明协议,AF_INET表示IPv4协议,SOCK_STREAM表示tcp协议
tcpSerSock = socket(AF_INET,SOCK_STREAM)

#绑定地址和端口,表示使用这个地址
#HOST为空字符串 本机所有ip,port为21567
tcpSerSock.bind(ADDR)

#使socket处于监听状态,参数大意是指,允许等待连接的客户端的最大数量
#这个TCP服务进程监听在本机所有ip,post为21567,等待客户端的连接
tcpSerSock.listen(5)

print('等待客户端连接')

tcpCliSock,addr = tcpSerSock.accept()
print('连接来自:',addr)
while True:
    #阻塞式等待接受消息,BUFSIZ指定了一次最多获取多少byte的消息
    #返回的式bytes类型
    #缺省的式阻塞模式,可以设置socket,为nonblocking
    data=tcpCliSock.recv((BUFSIZ))
    #当对方关闭连接的时候,返回空bytes
    if not data:
        tcpCliSock.close()
        break
    #接受到的是bytes类型,需要解码
    rstr = data.decode()
    print(rstr)


    tcpCliSock.sendall(f'**{rstr}'.encode())

tcpSerSock.close()
















