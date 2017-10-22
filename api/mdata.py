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

# TODO : generate hash from visible password

with open('./data/users.json', encoding=ENC) as data_file:
    users = json.load(data_file)
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

# Design patterns sur MongoDB :

# Pour les aggregations : remplacer le ObjectId par l'url avec le uuid quand le client ne veut pas voir les détails, sinon faire l'aggregation les documents adéquats
# Exemple url : afficher un auteur avec la liste de ses publications, cliquer sur le titre de la publication redirige vers celle-ci, au complet
# Exemple détails : afficher une section "commentaires de lecteur" qui montrera un lecteur avec tous ses commentaires et non juste un lienmenant  au commentaire

# Utiliser GridFS pour conserver des fichiers supérieurs à 16MB