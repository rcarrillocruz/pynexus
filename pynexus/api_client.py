import requests

class ApiClient:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

