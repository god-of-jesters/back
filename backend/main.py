from flask import Flask
from flask_restful import Api, Resource
app = Flask(__name__)
api = Api()
class Main(Resource):
    def get(self, name):
        if name == 'h':
            return {"answer" : "yes"}
        else:
            return "klsdv"
api.add_resource(Main, '/<name>')
api.init_app(app)