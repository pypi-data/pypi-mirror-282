import requests


def get_employees(id: str, host: str = "http://employees", port: int = 4100):
    """Wrapper function to get employees from the Flask app."""
    response = requests.get(f"{host}:{port}/api/v1/employees/{id}")
    return response.json()
