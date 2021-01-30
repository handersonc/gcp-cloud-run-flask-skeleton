"""
schemas/wagtail_document_base.py

Author: Handerson Contreras
"""
import json
import logging
import base64
from marshmallow import Schema, fields, post_load
from database.models.user import User

class ExampleSchema(Schema):
    """User Enrollments"""
    email = fields.Email(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)
    class Meta:
        strict = True
    
