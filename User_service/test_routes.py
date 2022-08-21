
# import json
# from multiprocessing.context import assert_spawning
# import requests
# from jsonschema import validate
# from jsonschema import Draft6Validator
# import test_schemas
# from flask import jsonify

# class TestRoutes:

#     URL = 'http://127.0.0.1:5001/user/'
#     user_credentials=  '{"username": "Kritikpancholi@gmail.com" , "password": "1234"}'
#     user_credentials_invalid=  '{"username": "invalid@gmail.com" , "password": "1234"}'
#     user= json.loads(
#         user_credentials
#         )
#     invalid_user= json.loads(user_credentials_invalid)
#     TOKEN= 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiI3YTk3MmUwZS1lZmI5LTQ4ZjEtODE5OS0xYjJhMTExMmY0OTgiLCJleHAiOjE2NjA5OTc5NjV9.QEOGOebvG4v9UDJM0yb27b2jK6kN8DOW9K2x2LKkYXQ'
    
#     expected_response_200 = {
#     "id": 1,
#     "admin": True,
#     "public_id": "7a972e0e-efb9-48f1-8199-1b2a1112f498",
#     "username": "Kritikpancholi@gmail.com"
#     }

#     def test_get_token_200(self):

#         resp= requests.get(self.URL+'login',json=self.user)
#         assert resp.status_code == 200
#         assert 'token' in resp.json()

#     def test_invalid_user_401(self):
#         resp= requests.get(self.URL+'login',json=self.invalid_user)
#         assert resp.status_code == 401

#     def test_show_all_users_200(self):
#         resp = requests.get(self.URL+'show_user')
#         assert resp.status_code == 200
#         validate(instance=resp, schema=test_schemas.show_all_users_schema_200)
#         # validate(instance=resp, schema=test_schemas.show_users_schema_200)

#     def test_get_user_200(self):
#         resp= requests.get(self.URL+'current_user', headers={"x-access-token":self.TOKEN})
#         assert resp.status_code == 200
#         resp_json= resp.json()
#         assert resp_json['id'] == 1
#         assert resp_json == self.expected_response_200
    
