"""
schemas/wagtail_document_base.py

Author: Handerson Contreras
"""
import json
import logging
import base64
from marshmallow import Schema, fields, post_load


class EnrollmentSchema(Schema):
    """Enrollments"""
    course_id = fields.Int(
        required=True, data_key='courseId')
    external_course_key = fields.Str(
        required=True, data_key='externalCourseKey')
    external_person_key = fields.Str(
        required=True, data_key='externalPersonKey')
    role = fields.Str(required=True, data_key='role')
    available_ind = fields.Str(required=True, data_key='availableInd')
    row_status = fields.Str(required=True, data_key='rowStatus')
    data_source_key = fields.Str(required=True, data_key='dataSourceKey')

    class Meta:
        strict = True


class ExampleSchema(Schema):
    """User Enrollments"""
    external_person_key = fields.Str(
        required=True, data_key='externalPersonKey')
    user_id = fields.Str(required=True, data_key='userId')
    email = fields.Email(required=True, data_key='email')
    first_name = fields.Str(required=True, data_key='firstName')
    last_name = fields.Str(required=True, data_key='lastName')
    system_role = fields.Str(required=True, data_key='systemRole')
    institution_role = fields.Str(required=True, data_key='institutionRole')
    available_ind = fields.Str(required=True, data_key='availableInd')
    row_status = fields.Str(required=True, data_key='rowStatus')
    data_source_key = fields.Str(required=True, data_key='dataSourceKey')
    enrollments = fields.List(fields.Nested(EnrollmentSchema))
    profile_id = fields.Str(required=True, data_key='profileId')
    program_id = fields.Int(required=True, data_key='programId')

    class Meta:
        strict = True
