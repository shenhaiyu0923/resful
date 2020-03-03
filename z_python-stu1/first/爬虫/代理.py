import urllib.request
def use_proxy(url,proxy_addr):
    proxy=urllib.request.ProxyHandler({"http":proxy_addr})  #设置代理
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)   #添加为全局
    data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
    return  data
proxy_addr="112.85.171.99:9999"    #代理ip经常无效
url="http://www.baidu.com"
data=use_proxy(url,proxy_addr)
print(len(data))


