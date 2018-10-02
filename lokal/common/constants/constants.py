import os

POST_DB_HOST = os.environ.get('POST_DB_HOST', 'localhost')
POST_DB_PORT = os.environ.get('POST_DB_PORT', '27017')
POST_DB_USERNAME = os.environ.get('POST_DB_USERNAME', 'root')
POST_DB_PWD = os.environ.get('POST_DB_PWD', 'root')

DEFAULT_MONGO_DB = 'lokal'