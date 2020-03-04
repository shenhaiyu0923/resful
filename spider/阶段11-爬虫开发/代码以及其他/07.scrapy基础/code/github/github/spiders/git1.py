# -*- coding: utf-8 -*-
import scrapy


class Git1Spider(scrapy.Spider):
    name = 'git1'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/exile-morganna']

    def start_requests(self):
        url = self.start_urls[0]
        temp = '_ga=GA1.2.1190047373.1543731773; _octo=GH1.1.1199554731.1543731773; user_session=6RCB6AkOT97lY9QXs98mHgHY6m8IScKjQPsf0i70K6GmSeeM; __Host-user_session_same_site=6RCB6AkOT97lY9QXs98mHgHY6m8IScKjQPsf0i70K6GmSeeM; logged_in=yes; dotcom_user=exile-morganna; _device_id=337049c7fc9520c4dbf2b5bdae3f2324; tz=Asia%2FShanghai; has_recent_activity=1; _gh_sess=bFl1RVN1RE9WTlBRVWthWjlBTFBaK0cySWRrV3lVL1FNTWdONG02WnFDTXpqWTVmeXdzWnI0Tk83dUtJY3BMc0xhMWdseHU4aDMwemFoMzRzNnB6UHZpV1hzUk8zbzlhNXozMURCdFozSTZtaWFOWEZmWklsb0FoK2NlM0IrWHRTcGtNUEJnbDlLOWFxSHpCVW1JY1ZxaFBDWlZCcEp5L00wOG5ycnhWWGcrSHZHOEZCdjdIK1ZxM1FBODkyT1JBbGxUTTJ6RTlLZDN0KytVRndXaWc1T0ErUTJzKzhpRGFpVVA0M3ZQSTN2d2prN2VzYjNSR1o1SXdUVURPTjRYYi0tcFJ1S0FoQVRSSE9INVZuOHlwUmRVZz09--d4ff9d6202137936d6c3968e2e5ef5a5b1f54ce7'
        cookies = {data.split('=')[0]:data.split('=')[-1]for data in temp.split('; ')}

        yield scrapy.Request(
            url=url,
            cookies=cookies
        )

    def parse(self, response):
        with open("git_with_cookies.html", "w")as f:
            f.write(response.text)
