from flask import request
from flask_api import status
from bson.json_util import loads, dumps
from pymongo import MongoClient
import json
from jsonschema import validate, ValidationError, SchemaError
import utils as u

# TODO IMPORTANT : use flask_restful for a real flask api (big refactor)
# TODO : refactor routes
# TODO : discuss about before_request and after_this_request decorators for response and headers settings
# TODO : Custom response class. Link  : https://blog.miguelgrinberg.com/post/customizing-the-flask-response-class
# TODO : discuss about the terminology in responses messages
# (example : what to return when it's the right email but wrong password ?)
# TODO : handle errors when mongodb is off during an request

class Route:
    def __init__(self, app):
        client = MongoClient('mongodb://localhost:27017/')
        db = client.magazine

        @app.route("/", methods=['GET'])
        def index():
            return "Bienvenue sur la page d'accueil du Magazine. Le site est actuellement en construction"

        @app.route("/login", methods=['POST'])
        def login():
            # TODO : add response creation in middleware logic (like before_request decorator)
            res = app.response_class(headers=None, mimetype="json", direct_passthrough=False)
            login_data = loads(request.data)

            # Validation
            with open('./schemas/loginSchema.json', encoding='utf-8') as data_file:
                login_schema = json.load(data_file)

            try:
                validate(login_data, login_schema)
            except ValidationError as e:
                res.status_code = status.HTTP_400_BAD_REQUEST
                res.response("wrong login form model provided")
                return res
            except SchemaError as e:
                print(e)
                res.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
                res.response("Error server")
                return res

            # TODO : custom fetchers
            del login_data['password'] # TODO : find best way ?

            result_query = db.users.find_one(login_data)

            if result_query is None:
                res.status_code = status.HTTP_401_UNAUTHORIZED
                res.response("Wrong login")
            elif False:
                # TODO : Compare passwords and return 401 if wrong password
                res.status_code = status.HTTP_401_UNAUTHORIZED
                res.response("Wrong password")
            else:
                res.status_code = status.HTTP_200_OK
                res.response = dumps({"user": result_query, "jwt": u.get_auth_token(result_query['username'])})

            return res

        @app.route("/magazine", methods=['GET'])
        def get_magazine():
            # TODO : Discuter des données contenues dans l'accueil du magazine

            return "Magazine"

        @app.route("/users/", methods=['GET'])
        def get_users():
            # TODO : add response creation in middleware logic (like before_request decorator)
            res = app.response_class(headers=None, mimetype="json", direct_passthrough=False)
            res.status_code = status.HTTP_200_OK
            res.response = dumps(db.users.find())

            return res

        @app.route("/posts/", methods=['GET'])
        def get_posts():
            # TODO : add response creation in middleware logic (like before_request decorator)
            res = app.response_class(headers=None, mimetype="json", direct_passthrough=False)
            res.status_code = status.HTTP_200_OK
            res.response = dumps(db.posts.find())

            return res

        @app.route("/posts/", methods=['POST'])
        def add_post():
            # TODO : add response creation in middleware logic (like before_request decorator)
            res = app.response_class(headers=None, mimetype="json", direct_passthrough=False)
            res.status_code = status.HTTP_201_CREATED
            res.response = dumps(db.posts.find())

            return 'post added'

        @app.route("/posts/<int:uuidPost>", methods=['GET'])
        def get_post(uuid_post):
            # TODO : add response creation in middleware logic (like before_request decorator)
            res = app.response_class(headers=None, mimetype="json", direct_passthrough=False)
            res.status_code = status.HTTP_200_OK
            # res.response = dumps(db.posts.find())

            result_query = dumps(db.posts.find(uuid_post))
            res = app.response_class(response=result_query, status=200, headers=None, mimetype="json", direct_passthrough=False)

            return res