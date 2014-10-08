import requests

class ApiClient:
    def __init__(self, host, username, password):
        self.uri = host + '/nexus/service/local/'
        self.username = username
        self.password = password

    def get_all_repositories(self):
        r = requests.get(self.uri + 'all_repositories', headers={'Accept': 'application/json'})

        return r

    def get_user_repositories(self):
        r = requests.get(self.uri + 'repositories', headers={'Accept': 'application/json'})

        return r

    def get_status(self):
        r = requests.get(self.uri + 'status', headers={'Accept': 'application/json'})
        
        return r

    def get_users(self):
        r = requests.get(self.uri + 'users', auth=(self.username, self.password), headers={'Accept': 'application/json'})

        return r

    def get_user(self, user_id):
        r = requests.get(self.uri + 'users' + '/' + user_id, auth=(self.username, self.password), headers={'Accept': 'application/json'})

        return r

    def get_roles(self):
        r = requests.get(self.uri + 'roles', auth=(self.username, self.password), headers={'Accept': 'application/json'})

        return r

    def get_role(self, role_id):
        r = requests.get(self.uri + 'roles' + '/' + role_id, auth=(self.username, self.password), headers={'Accept': 'application/json'})

        return r

    def get_repo_groups(self):
        r = requests.get(self.uri + 'repo_groups', headers={'Accept': 'application/json'})

        return r
