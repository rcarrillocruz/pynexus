import os, sys
sys.path.append(os.path.abspath('..'))

import unittest
from mock import patch
from pynexus import api_client

class NexusTest(unittest.TestCase):

    def test_constructor_appends_base(self):
        n = api_client.ApiClient('http://test.com', 'testuser', 'testpwd')
        self.assertEquals(n.uri, 'http://test.com/nexus/service/local/')
        
    @patch.object(api_client.requests, 'get')    
    def test_get_users_return_list_with_just_anonymous_user(self, mock_get):
        mock_output = u'{"data":[{"resourceURI":"http://test.com/nexus/' \
                       'service/local/users/anonymous","userId":"anonymous",' \
                       '"firstName":"Nexus","lastName":"Anonymous User",' \
                       '"status":"active","email":"changeme2@yourcompany.com"' \
                       ',"roles":["anonymous","repository-any-read"]}'

        mock_get.return_value = mock_output
        n = api_client.ApiClient('http://test.com', 'testuser', 'testpwd')
        result = n.get_users()
        self.assertEqual(result, mock_output)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
