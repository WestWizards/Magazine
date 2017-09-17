from bson.json_util import loads, dumps
from pymongo import MongoClient


class Route:
    def __init__(self, app):
        client = MongoClient('mongodb://localhost:27017/')
        db = client.magazine

        @app.route("/")
        def index():
            return "Bienvenue sur la page d'accueil du Magazine. Le site est actuellement en construction"

        @app.route("/magazine")
        def get_magazine():
            return "Magazine"

        @app.route("/users/")
        def get_users():
            print("debug get_users")
            result_query = dumps(db.users.find())
            client.close()
            res = app.response_class(response=result_query, status=200,headers=None, mimetype="json", direct_passthrough=False)

            return res
