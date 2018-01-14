import os

from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from route import Route

login_manager = LoginManager()

app = Flask(__name__)
CORS(app)
router = Route(app)
# TODO : newsletter system (news = Newsletter(app)
# TODO : use flask-login for auth logic

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


