"""
schemas/wagtail_document_base.py

Author: Handerson Contreras
"""
import json
import logging
import base64
from marshmallow import Schema, fields, post_load

class ExampleSchema(Schema):
    """User Enrollments"""
    email = fields.Email(required=True, data_key='email')
    first_name = fields.Str(required=True, data_key='firstName')
    last_name = fields.Str(required=True, data_key='lastName')
    class Meta:
        strict = True
