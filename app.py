from flask import Flask
from flask_restful import Resource, Api
from keys import apiKey
from pyrebase import pyrebase


app = Flask(__name__)
api = Api(app)

app.debug = True


config = {
    "apiKey": apiKey,
    "authDomain": "bdgm-test.firebaseapp.com",
    "databaseURL": "https://bdgm-test.firebaseio.com",
    "storageBucket": "bdgm-test.appspot.com",
    # "serviceAccount": "/Users/Valerie/Desktop/NorthCoders/bdgm-test-firebase-adminsdk-i9eq9-e382b6fb7b.json"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

all_users = db.child("users").get()


@app.route('/')
def hello_world():
    return 'Hello, World!'


class HelloWorld(Resource):
    def get(self):
        return (all_users.val())


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run()
