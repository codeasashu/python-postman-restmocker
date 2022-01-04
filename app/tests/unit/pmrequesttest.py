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

    def test_getcontenttype_returns_content_type(self):
        mypmrequest = pmrequest(self.mockdataprovider)
        content_type = mypmrequest.getHeader('Content-Type')
        self.assertEqual('application/x-www-form-urlencoded', content_type)

    def test_getbody_returns_body(self):
        mypmrequest = pmrequest(self.mockdataprovider)
        body_params = mypmrequest.getBody()
        for param in body_params:
            self.assertEqual('data', param['key'])
            self.assertEqual(
                '{"key": "1_zoho_client_id"}',
                param['value']
            )

    def test_get_url_return_url(self):
        mypmrequest = pmrequest(self.mockdataprovider)
        self.assertEqual(
            'http://localhost/memcache/get',
            mypmrequest.getUri()
        )

        self.mockdataprovider['url']['query'][0]['disabled'] = False
        mypmrequest = pmrequest(self.mockdataprovider)
        self.assertEqual(
            'http://localhost/memcache/get?a=b',
            mypmrequest.getUri()
        )

if __name__ == '__main__':
    unittest.main()
