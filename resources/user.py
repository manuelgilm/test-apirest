from flask_restful import Resource 
from stable_baselines import DDPG
class User(Resource):

    def get(self):
        return {'message':'Here is importing stable-baselines package'}