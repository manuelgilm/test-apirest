from flask_restful import Resource 
import json
class User(Resource):

    def get(self):
        return {'message':'This is a message'}