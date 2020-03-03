# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
from Douban.settings import USER_AGENT_LIST,PROXY_LIST
from scrapy import signals
import base64

# 定义一个中间件类
class RandomUserAgent(object):

    def process_request(self, request, spider):

        # print(request.headers['User-Agent'])
        ua = random.choice(USER_AGENT_LIST)
        request.headers['User-Agent'] = ua


class RandomProxy(object):

    def process_request(self, request, spider):
        proxy = random.choice(PROXY_LIST)
        print(proxy)
        if 'user_passwd' in proxy:
            # 对账号密码进行编码，python3中base64编码的数据必须是bytes类型，所以需要encode
            b64_up = base64.b64encode(proxy['user_passwd'].encode())
            # 设置认证
            request.headers['Proxy-Authorization'] = 'Basic ' + b64_up.decode()
            # 设置代理
            request.meta['proxy'] = proxy['ip_port']
        else:
            # 设置代理
            request.meta['proxy'] = proxy['ip_port']