import requests
from lxml import etree
# 引入模块
import os
import time
def mkdir(path):
    # 判断目录是否存在
    # 存在：True
    # 不存在：False
    folder = os.path.exists(path)
    # 判断结果
    if not folder:
        # 如果不存在，则创建新目录
        os.makedirs(path)
        print('-----创建成功-----')
    else:
        # 如果目录已存在，则不创建，提示目录已存在
        # print(path + '目录已存在')
        pass

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
    "referer": "https://www.mzitu.com/tag/ugirls"#反爬虫第二招
}
#//*[@id="pins"]/li[1]/a
#//*[@id="pins"]/li[1]/a/img
for i in range(1,223):
    # 1. 请求妹子图拿到HTML数据
    response = requests.get("https://www.mzitu.com/page/"+str(i), headers=headers)
    #'https://www.mzitu.com/185752'
    # 2. 抽取想要数据 图片标题，图片链接
    html = etree.HTML(response.text) # 整理对象
    urls = html.xpath('//li/a[@target="_blank"]/@href')
    for j in range(0, len(urls)):
        for k in range(1,16):
            url=urls[j]+"/"+str(k)
            print(url)
            response = requests.get(url, headers=headers)
            html = etree.HTML(response.text)  # 整理对象
            alt_list = html.xpath('//div[@class="main-image"]/p/a/img/@alt')#名字
            src_list = html.xpath('//div[@class="main-image"]/p/a/img/@src')
            #src_list = html.xpath('//img[@width="700"]/@src')#图片
            for alt, src in zip(alt_list, src_list):
                # 3. 下载图片
                res = requests.get(src, headers=headers)
                # 4. 保存图片
                path = 'e:/xxoo/test'
                mkdir(path)
                print(str(k))
                fileName = "e:/xxoo/test/"+str(k)+ alt+".jpg"
                print("正在保存图片文件：{}".format(fileName))
                with open(fileName, "wb") as f:
                    f.write(res.content)
                    time.sleep(1)
