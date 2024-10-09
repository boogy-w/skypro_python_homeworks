import pytest
from api_client import ApiClient

client = ApiClient()

def test_create_project_positive():
    payload = {
        "title": "New Project"
    }
    response = client.create_project(payload)
    assert response.status_code == 201
    project_data = response.json()
    assert "id" in project_data

def test_create_project_negative():
    payload = {}
    response = client.create_project(payload)
    assert response.status_code == 400  # Предполагается, что поля обязательны

def test_get_projects_positive():
    response = client.get_projects()
    assert response.status_code == 200

def test_update_project_positive():
    # Создание проекта для теста
    create_response = client.create_project({"title": "Project To Update"})
    project_id = create_response.json()["id"]

    update_data = {
        "title": "Updated Project Name"
    }
    response = client.update_project(project_id, update_data)
    assert response.status_code == 200
    project_data = response.json()
    assert "id" in project_data

def test_update_project_negative():
    project_id = "non_existent_id"
    update_data = {
        "title": "New Name"
    }
    response = client.update_project(project_id, update_data)
    assert response.status_code == 404  # Предполагается, что проект не найден

def test_get_project_positive():
    # Создание проекта для теста
    create_response = client.create_project({"title": "Project To Retrieve"})
    project_id = create_response.json()["id"]

    response = client.get_project(project_id)
    assert response.status_code == 200

def test_get_project_negative():
    project_id = "non_existent_id"
    response = client.get_project(project_id)
    assert response.status_code == 404  # Предполагается, что проект не найден