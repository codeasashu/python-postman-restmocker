from context import pmresponse
import json
import unittest
import mock


class pmresponseTestSuite(unittest.TestCase):

    def setUp(self):
        self.mockdataprovider = json.loads(r'{ "name": "Get memcache data", "_postman_previewlanguage": "json", "header": [], "cookie": [], "body": "{\n    \"status\": \"success\",\n    \"result\": {\n        \"1_zoho_access_token\": \"abc\"\n    }\n}" }')

    def test_get_code_return_response_code(self):
        mypmresponse = pmresponse(self.mockdataprovider)
        self.assertEqual(200, mypmresponse.getCode())

    def test_get_header_return_response_code(self):
        mypmresponse = pmresponse(self.mockdataprovider)
        self.assertEqual('text/html', mypmresponse.getHeader('Content-Type'))

        self.mockdataprovider['header'] = []
        self.mockdataprovider['header'].append(
            dict({'key': 'Content-Type', 'value': 'application/json'})
        )
        mypmresponse = pmresponse(self.mockdataprovider)
        self.assertEqual(
            'application/json',
            mypmresponse.getHeader('Content-Type')
        )

    def test_getbody_returns_body(self):
        mypmresponse = pmresponse(self.mockdataprovider)
        jsonstr = json.loads('{ "status": "success", "result": { "1_zoho_access_token": "abc" } }')
        self.assertEqual(json.dumps(jsonstr), mypmresponse.getBody())

if __name__ == '__main__':
    unittest.main()
