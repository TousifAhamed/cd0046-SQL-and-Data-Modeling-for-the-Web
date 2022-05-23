import os
from settings import DB_NAME, DB_USER, DB_PASSWORD, DB_PORT
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://'+DB_USER+':'+DB_PASSWORD+'@localhost:'+ DB_PORT +'/'+DB_NAME
