import os
import json
from .example_walker import example_walker


class Parser(object):

    """Open a collection file"""
    def openFile(self, filename):
        if not os.path.isfile(filename):
            raise Exception("File not found")
        self.pm_file = filename
        with open(self.pm_file, 'r') as f:
            self.pm_content = json.loads(f.read())
        f.close()

    # Gets a postman example file
    def getFile(self):
        return self.pm_file

    # Returns content of read file
    def getContent(self):
        return json.dumps(self.pm_content)

    def getExamples(self):
        examplewalker = example_walker(self.pm_content)
        return examplewalker.getExamples(flatten=True)
