from bson.json_util import loads, dumps
from pymongo import MongoClient

# TODO : réduire les redondances de code

class Route:
    def __init__(self, app):
        client = MongoClient('mongodb://localhost:27017/')
        db = client.magazine

        @app.route("/")
        def index():
            return "Bienvenue sur la page d'accueil du Magazine. Le site est actuellement en construction"

        @app.route("/magazine")
        def get_magazine():
            # TODO : Discuter des données contenues dans l'accueil du magazine

            return "Magazine"

        @app.route("/users/")
        def get_users():
            print("debug get_users")
            result_query = dumps(db.users.find())
            res = app.response_class(response=result_query, status=200,headers=None, mimetype="json", direct_passthrough=False)

            return res

        @app.route("/posts/", methods=['GET'])
        def get_posts():
            print("debut get posts")
            result_query = dumps(db.posts.find())
            res = app.response_class(response=result_query, status=200,headers=None, mimetype="json", direct_passthrough=False)

            return res

        @app.route("/posts/", methods=['POST'])
        def add_post():
            print("debug add post")

            return 'post added'

        @app.route("/posts/<int:uuidPost>")
        def get_post(uuidPost):
            print("debug get post")
            result_query = dumps(db.posts.find(uuidPost))
            res = app.response_class(response=result_query, status=200, headers=None, mimetype="json", direct_passthrough=False)

            return res