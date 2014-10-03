import requests

class ApiClient:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

    def get_all_repositories(self):
        r = requests.get(self.host+'/nexus/service/local/repositories')

        return r
