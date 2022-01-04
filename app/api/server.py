import os
import json
from flask import Flask, render_template
from parser.parser import Parser

__UPLOADS_DIR = 'uploads'

app = Flask(__name__)


@app.route('/api')
def hello():
    return 'Postman REST Server localhost!'


@app.route('/api/examples')
def httpmock():
    filename = 'mock.json'
    uploadedFile = os.path.join(
        os.path.dirname(__file__), __UPLOADS_DIR, filename
    )

    parser = Parser()
    parser.openFile(uploadedFile)
    examples = parser.getExamples()
    requestnames = "<br>".join(
        [example.getUri() for example in examples
            if example.getUri() is not None]
    )
    # hell
    return requestnames

if __name__ == '__main__':
    print("Server running at" + os.environ['HOST'] + ":" + os.environ['PORT'])
    app.run(host=os.environ['HOST'], port=os.environ['PORT'], debug=True)
