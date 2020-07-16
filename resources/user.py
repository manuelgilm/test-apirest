from flask_restful import Resource 
import json
import tensorflow

class User(Resource):

    def get(self):
        return {'message':'Here is importing tensorflow package'}