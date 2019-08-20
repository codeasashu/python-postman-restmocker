from context import pmrequest
import json
import unittest
import mock


class PmrequestTestSuite(unittest.TestCase):

    def setUp(self):
        self.mockdataprovider = json.loads(r'{"method":"POST","header":[{"key":"Content-Type","name":"Content-Type","value":"application/x-www-form-urlencoded","type":"text"}],"body":{"mode":"formdata","formdata":[{"key":"data","value":"{\"key\": \"1_zoho_client_id\"}","type":"text"}]},"url":{"raw":"http://localhost/memcache/get","protocol":"http","host":["localhost"],"path":["memcache","get"],"query":[{"key":"a","value":"b","disabled":true}]}}')

    def test_get_method_return_method(self):
        mypmrequest = pmrequest(self.mockdataprovider)
        self.assertEqual('POST', mypmrequest.getMethod())

    def test_can_get_name_from_request(self):
        mypmrequest = pmrequest(self.mockdataprovider, 'memcache req')
        self.assertEqual('memcache req', mypmrequest.getName())

        mypmrequest = pmrequest(self.mockdataprovider)
        self.assertIsNone(mypmrequest.getName())

    def test_get_url_return_url(self):
        mypmrequest = pmrequest(self.mockdataprovider)
        self.assertEqual('http://localhost/memcache/get', mypmrequest.getUri())

        self.mockdataprovider['url']['query'][0]['disabled'] = False
        mypmrequest = pmrequest(self.mockdataprovider)
        self.assertEqual('http://localhost/memcache/get?a=b', mypmrequest.getUri())

if __name__ == '__main__':
    unittest.main()
