from flask import Flask 
from flask_restful import Api 

from resources.user import User

app = Flask(__name__)

api = Api(app)

api.add_resource(User, '/user')

if __name__ == "__main__":
    app.run()
