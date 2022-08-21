import json
import logging
import unittest
import requests
import test_schemas
from jsonschema import validate

user_credentials=  '{"username": "Kritikpancholi@gmail.com" , "password": "1234"}'
user_credentials_invalid=  '{"username": "invalid@gmail.com" , "password": "1234"}'
user= json.loads(
    user_credentials
    )
invalid_user= json.loads(user_credentials_invalid)

class TestAPI(unittest.TestCase):
    TOKEN= ''
    def __init__(self, methodName: str = ...) :
        super().__init__(methodName)
        res= requests.get(self.URL+'login',json=user)
        self.TOKEN= res.json()['token']
    URL = 'http://127.0.0.1:5001/user/'
 

    def test_01_login(self):
        res= requests.get(self.URL+'login',json=user)
        self.TOKEN = res.json()["token"]


   
    expected_response_200 = {
    "id": 1,
    "admin": True,
    "public_id": "7a972e0e-efb9-48f1-8199-1b2a1112f498",
    "username": "Kritikpancholi@gmail.com"
    }



    def test_02_get_token_200(self):

        resp= requests.get(self.URL+'login',json=user)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('token',resp.json())
        self.TOKEN = resp.json()["token"]

    def test_05_invalid_user_401(self):
        resp= requests.get(self.URL+'login',json=invalid_user)
        self.assertEqual(resp.status_code, 401)

    def test_03_show_all_users_200(self):
        resp = requests.get(self.URL+'show_user')
        self.assertEqual(resp.status_code, 200)
        validate(instance=resp, schema=test_schemas.show_all_users_schema_200)

    def test_04_get_user_200(self):

        resp= requests.get(self.URL+'current_user', headers={"x-access-token":self.TOKEN})
  
        self.assertEqual( resp.status_code , 200)
        resp_json= resp.json()
        self.assertEqual( resp_json['id'] , 1)
        self.assertDictEqual( resp_json, self.expected_response_200)

  

if __name__ == "__main__":
    unittest.main()
