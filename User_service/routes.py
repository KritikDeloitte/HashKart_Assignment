from asyncio.windows_events import NULL
import datetime
import imp
from pickle import NONE
from urllib import response
from app import app, db
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import jwt
from functools import wraps
from flask import request, jsonify, make_response

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            app.logger.error('Token is missing!')
            return jsonify({'message' : 'Token is missing!'}), 401

        try: 
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            app.logger.error('Token is invalid!')
            return jsonify({'message' : 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated


@app.route('/user/register', methods=['POST'])
def create_user():
    app.logger.info('register_user')
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user= User(public_id=str(uuid.uuid4()), username=data['username'], password=hashed_password, admin=False)
    db.session.add(new_user)
    db.session.commit()
    response  = jsonify({'message' : 'New user created!'}), 201
    return response


@app.get('/user/show_user')
def get_all_users():
    users = User.query.all()

    output = []

    for user in users:
        user_data = {}
        user_data['id'] = user.id
        user_data['public_id'] = user.public_id
        user_data['username'] = user.username
        user_data['password'] = user.password
        user_data['admin'] = user.admin
        output.append(user_data)
    
    response = jsonify( output)
    return response

@app.route('/user/login', methods=['GET','POST'])
def login():
    app.logger.info('login')
    auth = request.get_json() 

    username = auth['username']

    password = auth['password']

    response = NONE
    if not username or not password:
        app.logger.error('Could not verify, Incorrect username or password')
        response = make_response(jsonify({'msg':'Username or Password invalid'}), 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    user = User.query.filter_by(username=username).first()

    
    app.logger.error('Could not verify')
    response = make_response( jsonify({'msg':'Username or Password invalid'}), 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})
    if user:
        if check_password_hash(user.password, password):
            token = jwt.encode({'public_id' : user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=120)}, app.config['SECRET_KEY'])

            response = jsonify({'token' : token.decode('UTF-8')})

    return response

@app.route('/user/current_user', methods=['GET'])
@token_required
def get_user(current_user):
    
    app.logger.info('get_user')
    user_data = {}
    user_data['id'] = current_user.id
    user_data['public_id'] = current_user.public_id
    user_data['username'] = current_user.username
    user_data['admin']= current_user.admin
    response = jsonify(user_data)
    return response

