from lokal.common.db import post_db
from lokal.common.constants import constants, urls

def fetch_post(payload):
    payload = payload if payload else {}
        
    cursor = post_db.post_db().get_posts_with_filter(payload)
    posts = None
    if cursor:
        posts = []
        for post in cursor:
            post['_id'] = str(post['_id'])
            posts.append(post)
    return posts

def insert_post(payload):
    return post_db.post_db().add_event(payload)
    




