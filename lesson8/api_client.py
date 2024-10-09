import requests
from config import API_URL, AUTH_TOKEN

class ApiClient:
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {AUTH_TOKEN}",
            "Content-Type": "application/json"
        }

    def create_project(self, data):
        return requests.post(f"{API_URL}/projects", json=data, headers=self.headers)

    def get_projects(self):
        return requests.get(f"{API_URL}/projects", headers=self.headers)

    def update_project(self, project_id, data):
        return requests.put(f"{API_URL}/projects/{project_id}", json=data, headers=self.headers)

    def get_project(self, project_id):
        return requests.get(f"{API_URL}/projects/{project_id}", headers=self.headers)