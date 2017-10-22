from flask import Flask
from flask_cors import CORS
from route import Route

app = Flask(__name__)
CORS(app)
router = Route(app)

# use Deployment Options instead of run for prod
if __name__ == '__main__':
    app.run(debug=True)