import os
from flask import Flask
from parser.parser import Parser

__UPLOADS_DIR = 'uploads'

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World 23!'

@app.route('/mock')
def httpmock():
    filename = 'mock.json'
    uploadedFile = os.path.join(
        os.path.dirname(__file__), __UPLOADS_DIR, filename
    )

    parser = Parser()
    parser.openFile(uploadedFile)
    examples = parser.getExamples()
    requestnames = ', '.join([example.getName() for example in examples])
    # hell
    return requestnames

if __name__ == '__main__':
    print("Server running at"+ os.environ['HOST'] +":"+ os.environ['PORT'])
    app.run(host=os.environ['HOST'], port=os.environ['PORT'], debug=True)
