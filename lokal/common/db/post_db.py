import pymongo
from pymongo import MongoClient
from lokal.common.constants import constants
from lokal.common.utils.response_messages import Logger

class post_db:
    class __post_db:
        _client = None
        _db = None

        def __init__(self):
            if not self._client:
                self._client = MongoClient(constants.POST_DB_HOST, int(constants.POST_DB_PORT))
            if not self._db:
                self._db = self._client[constants.DEFAULT_MONGO_DB]

        def get_db(self):
            return self._db

        def get_collection(self, collection_name):
            if self._db:
                return self._db[collection_name]
            else:
                return None

    instance = None

    def __init__(self):
        if not post_db.instance:
            post_db.instance = post_db.__post_db()

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def add_event(self, payload):
        posts_collection = post_db.instance.get_collection("posts")
        # _id will be automatically added by mongo
        title = payload['title'] if 'title' in payload else ''
        description = payload['description'] if 'description' in payload else ''
        location = payload['location'] if 'location' in payload else ''
        category = payload['category'] if 'category' in payload else ''
        insert_payload = {"title": title,
                          "description": description, "location": location, "category": category}
        try:
            posts_collection.insert_one(insert_payload)
        except Exception as e:
            Logger().exception("Exception {} occurred while inserting document".format(str(e)))
            return None    
        return {'inserted': True}

    def get_posts_with_filter(self, filters):
        posts_collection = post_db.instance.get_collection("posts")
        query_filter = generate_filter_query(filters)
        try:
            posts = posts_collection.find(filter=query_filter)
        except Exception as e:
            Logger().exception("Exception {} occurred while fetching documents".format(str(e)))
            return None    
        return posts
        


def generate_filter_query(filters):
    query_filter = {}
    if filters.get("category"):
        category_filter_type = filters.get("category").get("filter_type")
        if category_filter_type == 'or':
            query_filter["category"] = {"$in": filters.get("category").get("values")}
        else:
            query_filter["category"] = {"$all": filters.get("category").get("values")}
    if filters.get("location"):
        location_filter_type = filters.get("location").get("filter_type")
        if location_filter_type == 'or':
            query_filter["location"] = {"$in": filters.get("location").get('values')}
        else:
            query_filter["location"] = {"$all": filters.get("location").get('values')}
    return query_filter
