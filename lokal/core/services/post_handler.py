from lokal.common.utils.request_session import RequestSession
from lokal.core.controllers import post_controller


def fetch_filter_post(event, context):
    req_session = RequestSession(event)
    req_error = req_session.validate_authorized_request()
    if req_error:
        return req_error
    
    posts = post_controller.fetch_post(req_session.get_body())
    if posts is None:
        return req_session.generate_error_response(401,{'success': False})
    return req_session.generate_sqlalchemy_response(200, {'posts':posts,'success':True})


def insert_post(event, context):
    req_session = RequestSession(event)
    req_error = req_session.validate_authorized_request()
    if req_error:
        return req_error
    
    post_res = post_controller.insert_post(req_session.get_body())
    if not post_res:
        return req_session.generate_error_response(401,{'inserted': False})
    else:
        return req_session.generate_sqlalchemy_response(200, post_res)        

    

