from locust import HttpLocust,TaskSequence,task
from random import randint

class UserBehavior(TaskSequence):

    @task(1)
    def login(self):
        url = "en/v2/authentications"
        headers = {
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 6.0.1; VIVO X20 Build/V417IR) [,340fee311994e386,1583737416858-410961750665631264] lq-App Vova  android",
        }
        params = {
            "password": "96e79218965eb72c92a549dd5a330112",
            "username": "ning@tetx.com",
        }
        r = self.client.get(url, params=params, headers=headers)
        return r.json()

    # @task(2)
    # def all_user(self):
    #     self.client.get("books_drf")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 3000

if __name__ == "__main__":
    import os
    os.system("locust -f loc.py --web-host=127.0.0.1")

