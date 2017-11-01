from bson.json_util import loads, dumps
from pymongo import MongoClient
import bcrypt
import json
salt = bcrypt.gensalt()
INIT_MODE = "dev"
ENC = 'utf-8'

client = MongoClient('mongodb://localhost:27017/')
if INIT_MODE == "dev":
    client.drop_database('magazine')
db = client.magazine


with open('./data/users.json', encoding=ENC) as data_file:
    users = json.load(data_file)
for u in users:
    bin = u["password"].encode(ENC)
    u["password"] = bcrypt.hashpw(bin, bcrypt.gensalt()) # Question : self == "this"
db.users.insert_many(users)

with open('./data/posts.json', encoding=ENC) as data_file:
    posts = json.load(data_file)
db.posts.insert_many(posts)

with open('./data/sections.json', encoding=ENC) as data_file:
    sections = json.load(data_file)
db.sections.insert_many(sections)

with open('./data/comments.json', encoding=ENC) as data_file:
    comments = json.load(data_file)
db.comments.insert_many(comments)

client.close()