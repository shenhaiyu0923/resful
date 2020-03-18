from locust import HttpLocust,TaskSequence,task
from random import randint

class UserBehavior(TaskSequence):
    # @task(1)
    # def one_user(self):
    #     i=randint(1,3)
    #     self.client.get("books/{}".format(i))
    #     # params={
    #     #     "id":i,
    #     # }
    #     # self.client.get('books',params=params)

    @task(2)
    def all_user(self):
        self.client.get("books_drf")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 100
    max_wait = 500

if __name__ == "__main__":
    import os
    os.system("locust -f loc.py --web-host=127.0.0.1")

