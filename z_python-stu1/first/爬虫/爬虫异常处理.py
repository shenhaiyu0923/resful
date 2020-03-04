"""
301  永久性重定向
302重定向到临时url，非永久性
304请求的资源未更新
400非法请求
401请求未经授权
403禁止访问
404没有找到对应页面
500服务器内部错误
501服务器不支持实现请求所需要的功能

URLError   它包含httperror
1，连不上服务器
2，远程的url不存在
3，没有网络
4，触发了http的子类
"""
import urllib.error
import urllib.request

try:
    urllib.request.urlopen("http://blog.csdn.net")
except urllib.error.URLError as e:
    if hasattr(e,"code"):
        print(e.code)    #判断有没有code状态码
    if hasattr(e,"reason"):
        print(e.reason)   #打印原因