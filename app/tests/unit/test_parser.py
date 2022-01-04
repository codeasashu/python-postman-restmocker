from context import Parser
import unittest
import mock


class ParserTestSuite(unittest.TestCase):

    def setUp(self):
        self.collectionfile = 'a.txt'

    """Can open a postman example file"""
    @mock.patch('context.os.path')
    def test_openfile_can_get_content(self, mock_os_path):
        mock_os_path.isfile.return_value = True
        parser = Parser()
        parser.openFile(self.collectionfile)
        self.assertEqual(self.collectionfile, parser.getFile())
        self.assertIsNotNone(parser.getContent())
    
    """Exception thrown on file not found"""
    @mock.patch('context.os.path')
    def test_exception_thrown_on_file_not_found(self, mock_os_path):
        mock_os_path.isfile.return_value = False
        parser = Parser()
        self.assertRaises(Exception, parser.openFile, self.collectionfile)

if __name__ == '__main__':
    unittest.main()
