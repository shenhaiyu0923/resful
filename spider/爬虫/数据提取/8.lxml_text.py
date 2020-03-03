#coding:utf-8
from lxml import etree

text = ''' 
<div> 
    <ul> 
        <li class="item-1">
            <a href="link1.html">first item</a>
        </li> 
        <li class="item-1">
            <a href="link2.html">second item</a>
        </li> 
        <li class="item-inactive">
            <a href="link3.html">third item</a>
        </li> 
        <li class="item-1">
            <a href="link4.html">fourth item</a>
        </li> 
        <li class="item-0">
            <a href="link5.html">fifth item</a> 
    </ul> 
</div> '''

# 将html源码创建成element对象

html = etree.HTML(text)

# etree.HTML()能够自动补全html缺失的标签
print(etree.tostring(html))



# print(html)
# print(dir(html))

# print(html.xpath('//li[1]/a/text()'))
# print(html.xpath('//li[1]/a/@href'))

# text_list = html.xpath('//a/text()')
# link_list = html.xpath('//a/@href')
# print(text_list)
# print(link_list)
#
# for text,link in zip(text_list, link_list):
#     print(text,link)

# el_list = html.xpath('//a')
#
# for el in el_list:
#     # print(el.xpath('//text()')[0], el.xpath('//@href')[0])
#     print(el.xpath('./text()')[0], el.xpath('./@href')[0])
#     print(el.xpath('.//text()')[0], el.xpath('.//@href')[0])
#     # print(el.xpath('text()')[0], el.xpath('@href')[0])