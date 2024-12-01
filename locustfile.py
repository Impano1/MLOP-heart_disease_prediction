from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def predict(self):
        self.client.post("/predict", json={
            'Age': 63, 'Sex': 1, 'ChestPainType': 2, 'RestingBP': 145, 'Cholesterol': 233,
            'FastingBS': 1, 'RestingECG': 0, 'MaxHR': 150, 'ExerciseAngina': 0, 'Oldpeak': 2.3
        })