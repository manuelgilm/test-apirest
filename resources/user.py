from flask_restful import Resource 
import json
import stable_baselines

class User(Resource):

    def get(self):
        return {'message':'This is a message'}