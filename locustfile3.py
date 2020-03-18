# coding:utf-8
from locust import HttpLocust, TaskSet, task
from lxml import etree

class LoginDemo(TaskSet):
    '''用户行为描述'''
    def get_it_execution(self):
        result = {}
        h1 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        }
        self.client.headers.update(h1)
        r = self.client.get("/passport/login", verify=False)
        # 从返回html页面，解析出lt、execution
        dom = etree.HTML(r.content.decode("utf-8"))
        try:
            result["lt"] = dom.xpath('//input[@name="lt"]')[0].get("value")
            result["execution"] = dom.xpath('//input[@name="execution"]')[0].get("value")
            print(result)
        except:
            print("lt、execution参数获取失败！")
        return result

    def login(self, user, psw):
        result = self.get_it_execution()
        loginurl = "/passport/login"
        h2 = {
            "Referer": loginurl,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Origin": "https://account.chsi.com.cn",
            "Content-Length": "119",
            "Cache-Control": "max-age=0",
            "Upgrade-Insecure-Requests": "1",
            "Content-Type": "application/x-www-form-urlencoded"
            }
        body = {
            "username": user,
            "password": psw,
            "rememberMe": "true",
            "lt": result["lt"],
            "execution": result["execution"],
            "_eventId": "submit"
        }
        self.client.headers.update(h2)
        print(self.client.headers)
        r1 = self.client.post(loginurl, data=body, verify=False)
        # print(r1.text)

    @task(1)
    def test_login(self):
        # 测试数据
        user = "13888888888"
        psw = "111111"
        self.login(user, psw)

class websitUser(HttpLocust):
    task_set = LoginDemo
    host = "https://account.chsi.com.cn"
    min_wait = 3000  # 单位毫秒
    max_wait = 6000  # 单位毫秒

if __name__ == "__main__":
    import os
    os.system("locust -f locustfile3.py")