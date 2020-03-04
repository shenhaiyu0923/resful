# -*- coding: utf-8 -*-
import scrapy


class Git1Spider(scrapy.Spider):
    name = 'git1'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/shenhaiyu0923']

    def start_requests(self,):
        url = self.start_urls[0]
        temp = '_octo=GH1.1.526325787.1569747509; _ga=GA1.2.2133914681.1569747510; _device_id=5ea849ff87740319e182f7275061d39c; user_session=Ixv2GS6ld5pTh4B5Tgz_toASdSZ4djxMmjVnMMiAmc1_3h0V; __Host-user_session_same_site=Ixv2GS6ld5pTh4B5Tgz_toASdSZ4djxMmjVnMMiAmc1_3h0V; logged_in=yes; dotcom_user=shenhaiyu0923; has_recent_activity=1; tz=Asia%2FShanghai; _gat=1; _gh_sess=kiNnWb7%2BoaJcEbt4M21YpkWSguv2qZtrL%2Bpqgf40xbhMbyhVJovxKxP%2BA0zkmiLUJ9aiiQoc5I2lz2GHSF9PjTkcweSr1hkP6mMbCDurM5cUuXqU%2BZsMz4eZ%2F%2BmpOYL7umM8GrWriTZX1NMppOP3sFZHWegTZxWMe%2FTYye94gt%2ByJqaQZxqFdQaycHM2U2SW--RsQwOTdHnTytsu9B--IaRrWudKPtmfuiW0vHnlwA%3D%3D'
        cookies = {data.split('=')[0]:data.split('=')[-1]for data in temp.split('; ')}

        yield scrapy.Request(
            url=url,
            cookies=cookies
        )

    def parse(self, response):
        print(response.xpath('/html/head/title/text()').extract())