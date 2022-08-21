from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)

     
    def __init__(self, public_id, username, password,admin):
        self.username= username
        self.password= password
        self.public_id= public_id
        self.admin= admin