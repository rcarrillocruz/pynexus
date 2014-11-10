import requests
import json

class ApiClient:
    def __init__(self, host, username, password):
        self.uri = host + '/nexus/service/local'
        self.username = username
        self.password = password

    def __get(self, resource):
        r = requests.get(self.uri + '/' + resource, auth=(self.username, self.password), headers={'Accept': 'application/json'})

        return r

    def get_all_repositories(self):
        return self.__get('all_repositories')

    def get_user_repositories(self):
        r = self.__get('repositories')

        return r

    def create_hosted_repo(self, repo_id, repo_name, provider, storage_folder, 
                           deploy_policy='ALLOW_WRITE_ONCE', browseable=True, indexable=True, 
                           repo_policy='RELEASE', url_visible=True, not_found_cache_ttl=1440):

        payload = {'data': {'repoType': 'hosted', 'id': repo_id, 'name': repo_name, 'provider': provider, 
                            'repoPolicy': repo_policy, 'overrideLocalStorageUrl': storage_folder,
                            'writePolicy': deploy_policy, 'browseable': browseable,
                            'indexable': indexable, 'exposed': url_visible, 'notFoundCacheTTL': not_found_cache_ttl,
                            'providerRole':'org.sonatype.nexus.proxy.repository.Repository',
                            'downloadRemoteIndexes': False,'checksumPolicy': 'IGNORE'}}
        
        r = requests.post(self.uri + 'repositories', auth=(self.username, self.password), headers={'Accept': 'application/json', 'Content-Type': 'application/json'}, 
                          data=json.dumps(payload))

        return r 

    def get_status(self):
        r = self.__get('status')
        
        return r

    # TODO this will probably haunt me at some point, not sure if Nexux expects boolean values as strings or not
    def get_repository_statuses(self, forceCheck=False):
        r = requests.get(self.uri + 'repository_statuses', headers={'Accept': 'application/json'}, params={'forceCheck': forceCheck})

        return r

    def get_users(self):
        r = self.__get('users')

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
        r = self.__get('roles')

        return r

    def get_role(self, role_id):
        r = self.__get('roles' + '/' + role_id)

        return r

    def get_repo_groups(self):
        r = self.__get('repo_groups')

        return r

    def get_repo_group(self, group_id):
        r = self.__get('repo_groups' + '/' + group_id)

        return r

    def get_privileges(self):
        r = self.__get('privileges')

        return r

    def get_privilege(self, privilege_id):
        r = self.__get('privileges' + '/' + privilege_id)

        return r

    def get_schedules(self):
        r = self.__get('schedules')

        return r

    def get_schedule(self, schedule_id):
        r = self.__get('schedules' + '/' + str(schedule_id))

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
