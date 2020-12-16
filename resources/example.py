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


class ExampleResource(Resource):
    """POST to example resource"""

    @use_args(ExampleSchema())
    def post(self, payload):
        """user enrollments"""

        return {'message': 'Data uploaded'}, 200
