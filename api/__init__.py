from flask import Flask
from pymongo import MongoClient

from .route import Route
from .services import get_auth_token