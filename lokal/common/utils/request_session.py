from flask_restful import request
import json
from lokal.common.constants import constants

# from lokal.common.db.models import alchemy_encoder

class RequestSession():
    def __init__(self, req):
        self.req = req if req else {}
        self.auth_token = None
        self.params = {}
        self.headers = {}

    def validate_authorized_request(self, validateAuth=True, mandatory_params=[], optional_params=[], headers=[]):
        # Validate the flask request

        headers_dict = self.req.headers
        params_dict = self.req.args

        self.auth_token = headers_dict.get("Authorization")
        # One Can validate requests here using unique auth-token
        # Avoiding as this is not the requirement of LOKAL Assignment
        
        # if validateAuth and not self.auth_token:
        #     return self.generate_error_response(401, "Not authenticated")
        
        # One Can validate  mandatory-params, optional-params of requests here 
        # Avoiding as this is not the requirement of LOKAL Assignment
        for param in mandatory_params:
            value = params_dict.get(param)
            if not value:
                return self.generate_error_response(400, "Missing request fields - " + param)
            else:
                self.params[param] = value
        for param in optional_params:
            self.params[param] = params_dict.get(param)

        for header in headers:
            self.headers[header] = headers_dict.get(header)

    def get_auth_token(self):
        return self.auth_token

    def get_req_param(self, param):
        return self.params[param]

    def get_all_req_param(self):
        return self.params

    def get_req_header(self, header):
        return self.headers[header]

    def get_body(self):
        return self.req.get_json()
        

    def generate_error_response(self, http_code, message):
        return self.generate_sqlalchemy_response(http_code, message)

    def generate_success_response(self, http_code, message):
        return self.generate_sqlalchemy_response(http_code, {'message': message})

    def generate_redirect_response(self, location):
        return {'location': location}, 301, {'location': location}
        

    def generate_sqlalchemy_response(self, http_code, payload):
        json_string_payload = json.dumps(payload)
        json_payload = json.loads(json_string_payload)
        return self.generate_response(http_code, json_payload)

    def generate_response(self, http_code, payload=None):
        return payload, http_code
        
