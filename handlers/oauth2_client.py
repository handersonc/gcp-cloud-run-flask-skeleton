
from app import app


@app.route("/authorize")
def authorize():
    """Root route.

    Returns:
        Str: Simple hello world response
    """
    return "Hello World!"
