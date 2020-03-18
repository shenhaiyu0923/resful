from locust import HttpLocust,TaskSequence,task
from pprint import pprint
from random import randint

class UserBehavior(TaskSequence):

    @task(1)
    def byhy(self):
        data = {
            "username": "byhy",
            "password": "88888888",
        }
        url = 'http://127.0.0.1:8001/api/mgr/signin'
        r = self.client.get(url,  data=data)
        pprint(r.json())

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 3000

if __name__ == "__main__":
    import os
    os.system("locust -f loc.py --web-host=127.0.0.1")

