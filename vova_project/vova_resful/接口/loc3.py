from locust import HttpLocust, TaskSequence, task, TaskSet
from pprint import pprint
from random import randint
import os


'''
1. 实现登陆基本功能，输出响应，脚本正确
2. 多用户随机登陆：在doLogin方法里构造随机数据。  -LR：参数化  Jmeter ： 参数化
3. 添加初始化方法on_start:类似于构造方法，每个用户只运行一次
4. 添加检查点：断言
- 在请求方法中设置catch_response参数为True
- 调用success和feature方法标注成功或失败
'''
# 任务类
#class TestLogin(TaskSet):TaskSequence 继承自TaskSet
class TestLogin(TaskSequence):
    #任务开始前先自动执行的
    def on_start(self):
        # 请求正文接受的是字典，username=byhy&passwprd=88888888

        self.loginnData = [
            {'username': 'byhy', 'password': '88888888'},
            {'username': 'byhy1', 'password': '888888881'},]
        print('------on_start-------')

    @task
    def doLogin(self):
        # 1000以内的随机数，对用户数据长度3进行取余数，0，1，

        ranIndex = randint(1,1000) % len(self.loginnData)
        data = {
            "username": "byhy",
            "password": "88888888",
        }
        url = 'http://127.0.0.1:8001/api/mgr/signin'
        response = self.client.post(url,data=self.loginnData[ranIndex],catch_response = True)# catch_response = True 捕获响应

        if '"ret": 0' in response.text:
            response.success()
        else:
            response.failure(' Can not login!')

        print(self.loginnData[ranIndex]['username'])
        print(response.text)

class WebSite(HttpLocust):
    task_set = TestLogin
    min_wait = 1000
    max_wait = 3000


if __name__ == "__main__":
    os.system("locust -f loc3.py --web-host=127.0.0.1")















'''
class UserBehavior(TaskSequence):

    @task(1)
    def byhy(self):
        data = {
            "username": "byhy",
            "password": "88888888",
        }
        url = 'http://127.0.0.1:8001/api/mgr/signin'
        r = self.client.post(url,  data=data)
        pprint(r.json())

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 3000

if __name__ == "__main__":
    import os
    os.system("locust -f loc3.py --web-host=127.0.0.1")

'''