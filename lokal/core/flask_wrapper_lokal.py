from flask import request
from flask_restful import Resource
from lokal.core.services import post_handler

       
class Post(Resource):
    def post(self):
        return post_handler.insert_post(request, None)


class FilterPost(Resource):
    def post(self):
        return post_handler.fetch_filter_post(request, None)        


