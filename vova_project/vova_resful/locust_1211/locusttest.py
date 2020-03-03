#一月 Jan.January，二月 Feb. February，三月 Mar. March，四月 Apr. April，五月 May. May，六月 Jun. June，七月 Jul. July，八月 Aug. August，九月 Sept. September，十月 Oct. October，十一月 Nov. November，十二月 Dec. December

# coding=utf-8
import requests
from locust import HttpLocust,TaskSet,task
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class MyBlogs(TaskSet):
    # 访问我的博客首页
    @task(1)
    def get_blog(self):
        # 定义请求头
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

        req = self.client.get("/imyalost",  headers=header, verify=False)
        if req.status_code == 200:
            print("success")
        else:
            print("fails")

class websitUser(HttpLocust):
    task_set = MyBlogs
    min_wait = 3000  # 单位为毫秒
    max_wait = 6000  # 单位为毫秒

if __name__ == "__main__":
    import os
    os.system("locust -f locusttest.py --host=http://www.cnblogs.com")
