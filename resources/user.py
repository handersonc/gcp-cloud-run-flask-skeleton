"""
resources/enrollment.py

Author: Handerson Contreras
"""
import re
import logging
import os
from os import environ

# flask imports
from flask import request
from flask_restful import Resource
from webargs.flaskparser import use_args

# mashmallow imports
from marshmallow import ValidationError

from schemas.example import ExampleSchema
from database.repository.user_repository import UserRepository

from pubsub.pubsub_client import PubsubClient

class UserResource(Resource):
    """POST to example resource"""

    def get(self, user_id):
        """get user"""
        print('get')

        return {'message': 'one'}

    @use_args(ExampleSchema())
    def post(self, user):
        """create user"""

        print(user.email)
        UserRepository().create(user)

        PubsubClient().send_message('new-user', {
            'email': user.email,
            'data': 'Mailtrap service welcome you',
            'subject': 'Welcome %s' % user.first_name,
        })
        
        return {'message': 'Data uploaded'}, 200
    
    def put(self, user_id):
        """put user"""
        print('put')

        return {'message': 'put user'}

class UserListResource(Resource):

    def get(self):
        result = UserRepository().list()
        
        return {'data': ExampleSchema(many=True).dump(result)}
