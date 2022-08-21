from jsonschema import validate

show_users_schema_200={
  "$schema": "http://json-schema.org/draft-04/schema#",
  "properties": {
    "admin": {
      "type": "boolean"
    },
    "id": {
      "type": "integer"
    },
    "public_id": {
      "type": "string"
    },
    "username": {
      "type": "string"
    }
  },
  "required": [
    "admin",
    "id",
    "public_id",
    "username"
  ]
}
show_all_users_schema_200= {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "properties": {
                "users": {
                "type": "array",
                "items": [
                    {
                    "properties": {
                        "admin": {
                        "type": "boolean"
                        },
                        "id": {
                        "type": "integer"
                        },
                        "password": {
                        "type": "string"
                        },
                        "public_id": {
                        "type": "string"
                        },
                        "username": {
                        "type": "string"
                        }
                    },
                    "required": [
                        "admin",
                        "id",
                        "password",
                        "public_id",
                        "username"
                    ]
                    }
                ]
                }
            },
            "required": [
                "users"
            ]
        }