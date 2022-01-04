from context import Parser
from context import pmrequest
import os
import json
import unittest


class ParserTestSuite(unittest.TestCase):

    tmpFilename = 'collection-mockapis.json'

    def setUp(self):
        self.collectionfile = os.path.join(
            os.path.dirname(__file__), self.tmpFilename
        )

    """Can open a postman example file"""
    def test_openfile_can_get_content(self):
        parser = Parser()
        parser.openFile(self.collectionfile)
        self.assertEqual(self.collectionfile, parser.getFile())
        with open(self.collectionfile, 'r') as f:
            mockcontent = json.loads(f.read())
        self.assertEqual(
            json.dumps(mockcontent),
            parser.getContent()
        )
        f.close()

    """Can read json from collection file"""
    def test_can_read_json_from_collection_file(self):
        parser = Parser()
        parser.openFile(self.collectionfile)
        examples = parser.getExamples()
        urls = []
        for example in examples:
            self.assertIsInstance(example['request'], pmrequest)
            urls.append(example['request'].getUri())

        self.assertCountEqual([
            'http://localhost/memcache/get',
            'http://localhost/memcache/get',
            'http://localhost/memcache/get_or_set'
        ], urls)

if __name__ == '__main__':
    unittest.main()
