# settings.py
import os
import logging
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.DEBUG)

DEBUG = os.environ.get('DEBUG')