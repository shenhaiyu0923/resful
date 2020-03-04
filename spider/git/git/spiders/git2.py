# -*- coding: utf-8 -*-
import scrapy


class Git2Spider(scrapy.Spider):
    name = 'git2'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        token = response.xpath('//input[@name="authenticity_token"]/@value').extract_first()


        # 构造post数据
        post_data = {
            "commit": "Sign in",
            "utf8": "✓",
            "authenticity_token": token,
            "login": "shenhaiyu0923@yeah.net",
            "password": "guiji0923",
            "webauthn-support": "supported"
        }
        print(post_data)

        # 构造一个post请求对象
        yield scrapy.FormRequest(
            url='https://github.com/session',
            callback=self.login,
            formdata=post_data
        )

    def login(self, response):
        yield scrapy.Request(
            url='https://github.com/shenhaiyu0923',
            callback=self.check_login
        )

    def check_login(self, response):
        print(response.xpath('/html/head/title/text()').extract())


'''
commit: Sign in
utf8: ✓
authenticity_token: Di/ud/5eXr8YhK11iPOchW2mo94K6z+AAlwopvovuA2qGDDiaKb1xYfkCi76FPZJ2QZU2zicY6knTyvmgIVgmQ==
ga_id: 78847616.1583307843
login: shenhaiyu0923@yeah.net
password: guiji0923
webauthn-support: supported
webauthn-iuvpaa-support: unsupported
return_to: 
required_field_df5d: 
timestamp: 1583309920741
timestamp_secret: 0ca4f469e2ee8551938cd775fcb53b6c92ed08a01ab5392a038c513fe014144e
'''