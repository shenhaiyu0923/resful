# -*- coding": "utf-8 -*-
import scrapy


class Git2Spider(scrapy.Spider):
    name = 'git2'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        utf8 = response.xpath('//input[@name="utf8"]/@value').extract_first()
        authenticity_token = response.xpath('//input[@name="authenticity_token"]/@value').extract_first()
        webauthn = response.xpath('//input[@name="webauthn-support"]/@value').extract_first()
        commit = response.xpath('//input[@name="commit"]/@value').extract_first()

        # 构造post数据
        post_data = {
            "commit": commit,
            "utf8": utf8,
            "authenticity_token": authenticity_token,
            "login": "exile-morganna",
            "password": "1QAZ2wSX3edC4rfv",
            "webauthn - support": webauthn
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
            url='https://github.com/exile-morganna',
            callback=self.check_login
        )

    def check_login(self, response):

        with open("git_with_post.html", "w")as f:
            f.write(response.text)