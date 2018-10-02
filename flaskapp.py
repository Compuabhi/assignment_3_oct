from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from lokal.common.constants import urls
from lokal.core import flask_wrapper_lokal


app = Flask(__name__)
CORS(app)

api = Api(app)


#Add all routes here

api.add_resource(flask_wrapper_lokal.Post, urls.POST_EVENT)
api.add_resource(flask_wrapper_lokal.FilterPost, urls.FETCH_FILTER_POST)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
