from bson.json_util import loads, dumps
from pymongo import MongoClient
import bcrypt
import json
salt = bcrypt.gensalt()
INIT_MODE = "use"

client = MongoClient('mongodb://localhost:27017/')
if INIT_MODE == "use":
    client.drop_database('magazine')
db = client.magazine

# TODO : generate hash from visible password

with open('./data/users.json') as data_file:
    users = json.load(data_file)
db.users.insert_many(users)

with open('./data/posts.json') as data_file:
    posts = json.load(data_file)
db.posts.insert_many(posts)

with open('./data/sections.json') as data_file:
    sections = json.load(data_file)
db.sections.insert_many(sections)

client.close()