#locust testcases for sample-app
from locust import HttpLocust, TaskSet, task, between


class UserBehavior(TaskSet):

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.index()

    @task(1)
    def index(self):
        self.client.get("/")

    @task(2)
    def register(self):
        self.client.post("/register", {"name":"user123", "age":"25"})


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(1.0, 2.0)
