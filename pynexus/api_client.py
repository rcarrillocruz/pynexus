import requests

class ApiClient:
    def __init__(self, host, username, password):
        self.uri = host + '/nexus/service/local/'
        self.username = username
        self.password = password

    def get_all_repositories(self):
        r = requests.get(self.uri + 'all_repositories', headers={'Accept': 'application/json'})

        return r

    def get_status(self):
        r = requests.get(self.uri + 'status', headers={'Accept': 'application/json'})
        
        return r
