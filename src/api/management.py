from flask_restful import Resource, reqparse, request
from db.swen344_db_utils import *
from db.rideshare import*

class Init(Resource):
    def post(self):
        rebuildTables()

class Version(Resource):
    def get(self):
        return (exec_get_one('SELECT VERSION()'))