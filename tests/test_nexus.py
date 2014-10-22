import unittest
from pynexus import api_client

class NexusTest(unittest.TestCase):

    def test_constructor_appends_base(self):
        n = api_client.ApiClient('http://test.com', 'testuser', 'testpwd')
        self.assertEquals(n.uri, 'http://test.com/nexus/service/local/')
        
