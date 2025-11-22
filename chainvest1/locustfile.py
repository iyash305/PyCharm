from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)   # time between user actions

    @task
    def load_login_page(self):
        self.client.get("/Chainvest/BO/admin-login")
