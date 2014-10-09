import requests
import json

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

    # TODO this will probably haunt me at some point, not sure if Nexux expects boolean values as strings or not
    def get_repository_statuses(self, forceCheck=False):
        r = requests.get(self.uri + 'repository_statuses', headers={'Accept': 'application/json'}, params={'forceCheck': forceCheck})

        return r

    def get_users(self):
        r = requests.get(self.uri + 'users', auth=(self.username, self.password), headers={'Accept': 'application/json'})

        return r

    def get_user(self, user_id):
        r = requests.get(self.uri + 'users' + '/' + user_id, auth=(self.username, self.password), headers={'Accept': 'application/json'})

        return r

    def create_user(self, user_id, first_name, last_name, email, status, password, roles):
        payload = {'data': {'userId': user_id, 'firstName': first_name, 'lastName': last_name,
                            'email': email, 'status': 'active', 'password': password, 'roles': roles}} 

        r = requests.post(self.uri + 'users', auth=(self.username, self.password), headers={'Accept': 'application/json', 'Content-Type': 'application/json'}, 
                          data=json.dumps(payload))

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

    def get_repo_group(self, group_id):
        r = requests.get(self.uri + 'repo_groups' + '/' + group_id, headers={'Accept': 'application/json'})

        return r

    def get_privileges(self):
        r = requests.get(self.uri + 'privileges', auth=(self.username, self.password), headers={'Accept': 'application/json'})

        return r

    def get_privilege(self, privilege_id):
        r = requests.get(self.uri + 'privileges' + '/' + privilege_id, auth=(self.username, self.password), headers={'Accept': 'application/json'})

        return r

    def get_schedules(self):
        r = requests.get(self.uri + 'schedules', auth=(self.username, self.password), headers={'Accept': 'application/json'})

        return r

    def get_schedule(self, schedule_id):
        r = requests.get(self.uri + 'schedules' + '/' + str(schedule_id), auth=(self.username, self.password), headers={'Accept': 'application/json'})

        return r

    def get_artifact_pom(self, group_id, artifact_id, version, repository):
        params = {'g': group_id, 'a': artifact_id, 'v': version, 'r': repository}
        r = requests.get(self.uri + 'artifact/maven', headers={'Accept': 'application/json'}, params=params)

        return r

    def rebuild_group_metadata(self, group_id, path=''):
        r = requests.delete(self.uri + 'metadata/repo_groups/' + group_id + '/content/' + path, auth=(self.username, self.password), headers={'Accept': 'application/json'})

        return r

    def rebuild_repo_metadata(self, repository_id, path=''):
        r = requests.delete(self.uri + 'metadata/repositories/' + repository_id + '/content/' + path, auth=(self.username, self.password), headers={'Accept': 'application/json'})

        return r
