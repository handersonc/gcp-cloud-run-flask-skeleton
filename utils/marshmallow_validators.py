"""
utils/marshmallow_validators.py

Authors: Handerson Contreras
"""
from marshmallow import ValidationError

def must_not_be_blank(data):
    if not data:
        raise ValidationError("Data not provided.")