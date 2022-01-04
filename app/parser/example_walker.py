from collections import OrderedDict
from .pmrequest import pmrequest
from .pmresponse import pmresponse
import uuid


class example_walker(object):

    def __init__(self, content):
        self.content = content
        self.examples = self.walk(content['item'])

    def walk(self, content):
        mainexamples = []
        for item in content:
            if 'item' in item:
                mainexamples = self.walk(item['item'])
            elif ('response' in item) and (isinstance(item['response'], list)):
                itemname = item['name'] if 'name' in item else uuid.uuid1()
                myexample = []
                for example in item['response']:
                    parsedrequest = pmrequest(example['originalRequest'])
                    parsedresponse = pmresponse(example)
                    myexample.append(OrderedDict({
                        'name': itemname,
                        'request': parsedrequest,
                        'response': parsedresponse
                    }))
                mainexamples.append(myexample)
        return mainexamples

    def flatten(self, l):
        return [item for sublist in l for item in sublist]

    def getExamples(self, flatten=False):
        return self.flatten(self.examples) if flatten is True \
            else self.examples
