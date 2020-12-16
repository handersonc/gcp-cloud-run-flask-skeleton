
from flask import Blueprint

authorize_page = Blueprint('authorize_page', __name__)


@authorize_page.route('/authorize')
def authorize():
    """Root route.

    Returns:
        Str: Simple hello world response
    """
    return "Hello World!"
