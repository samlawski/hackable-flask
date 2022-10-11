from locust import HttpUser, task, between

class HelloWorldUser(HttpUser):
  wait_time = between(1, 2)

  @task
  def hello_world(self):
    self.client.get("/checkout")
      
  def on_start(self):
    self.client.post("/login", {"email":"locust@locust.com", "password":"asdfasdf1"})