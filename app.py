"""
app.py

Author: Handerson Contreras
"""

from os import environ

from flask import Flask
from flask_restful import Api

from handlers.errors import *
from handlers.oauth2_client import authorize_page

from resources.user import UserResource, UserListResource

from settings import *

app = Flask(__name__)
api = Api(app)
settings = app.config


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


@app.errorhandler(404)
@app.errorhandler(405)
def _handle_api_error(ex):
    return ex


# blueprints
app.register_blueprint(authorize_page)

# api resources
api.add_resource(UserListResource, '/api/v1/user')
api.add_resource(UserResource, '/api/v1/user/<user_id>')


if __name__ == "__main__":
    app.run(debug=DEBUG, host='0.0.0.0', port=int(environ.get('PORT', 8080)))
