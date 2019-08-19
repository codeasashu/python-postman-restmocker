import os
from flask import Flask

app = Flask(__name__)

debug = False if os.environ['APP_ENV'] == 'production' else True

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    print("Server running at"+ os.environ['HOST'] +":"+ os.environ['PORT'])
    app.run(host=os.environ['HOST'], port=os.environ['PORT'], debug=debug)
