from flask_api import status
import jwt
from bson.json_util import loads, dumps
import json
import bcrypt
from jsonschema import validate, ValidationError, SchemaError
SECRET_KEY = "$2y$10$fKFQh1xQRVfdjXt0aZOk3.heVLZoyLDuxprz2Z2KERV3mSzSXpxD."

schemas = {}


def init_schemas():

    with open('./schemas/loginSchema.json', encoding='utf-8') as data_file:
        schemas["login"] = json.load(data_file)
    with open('./schemas/signupSchema.json', encoding='utf-8') as data_file:
        schemas["signup"] = json.load(data_file)


def validate_request(req):
    url = req.url_rule.rule[1:]

    if req.method is not 'GET':
        req.data = loads(req.data)
        # TODO : validate and escape data

        try:
            validate(req.data, schemas[url])
        except ValidationError as e:
            req.err = {"err": "Wrong " + url + " model", "message": "Wrong " + url + " model provided",
                       "status": status.HTTP_400_BAD_REQUEST}
            return req
        except SchemaError as e:
            req.err = {"err": "Server error", "message": "Server error in " + url,
                       "status": status.HTTP_500_INTERNAL_SERVER_ERROR}
            return req

    return req


def create_default_response(app):
    # TODO : handle headers by endpoint
    res = app.response_class(headers=None, mimetype="json", direct_passthrough=False)
    return res


def validate_user_password(password, db_hash):
    # TODO : escape string password
    return bcrypt.checkpw(password, db_hash)


def get_auth_token(u):
    return jwt.encode({"username": u, }, SECRET_KEY, algorithm='HS256')

# def disconnectUser(u):
#     return jwt.

init_schemas()