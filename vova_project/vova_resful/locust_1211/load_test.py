from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):

    @task(1)
    def vova(self):
        self.client.get("/")



class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000

#   locust -f load_test.py --web-host="127.0.0.1"
if __name__ == "__main__":
    import os
    os.system("locust -f load_test.py --web-host=127.0.0.1")
