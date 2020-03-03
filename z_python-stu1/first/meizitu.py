import requests
from lxml import etree
import os
os.makedirs( "e:/b/c/d/" )
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
    "referer": "https://www.mzitu.com/tag/ugirls"
}

# 1. 请求妹子图拿到HTML数据
response = requests.get("https://www.mzitu.com/tag/ugirls/", headers=headers)

# 2. 抽取想要数据 图片标题，图片链接
html = etree.HTML(response.text) # 整理对象
alt_list = html.xpath('//img[@class="lazy"]/@alt')
src_list = html.xpath('//img[@class="lazy"]/@data-original')
for alt, src in zip(alt_list, src_list):
    # 3. 下载图片
    res = requests.get(src, headers=headers)

    # 4. 保存图片
   # fileName = "iphone\\" + alt + ".jpg"
    fileName = "e:/b/c/d/" + alt + ".jpg"
    print("正在保存图片文件：{}".format(fileName))
    with open(fileName, "wb") as f:
        f.write(res.content)