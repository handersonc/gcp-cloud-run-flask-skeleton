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


class UserResource(Resource):
    """POST to example resource"""

    def get(self, user_id):
        """get user"""
        print('get')

        return {'message': 'user'}

    @use_args(ExampleSchema())
    def post(self, payload):
        """create user"""

        return {'message': 'Data uploaded'}, 200
    
    def put(self, user_id):
        """get user"""
        print('put')

        return {'message': 'put user'}
