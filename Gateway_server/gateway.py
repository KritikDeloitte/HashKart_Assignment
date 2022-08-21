from urllib import request, response
from flask import Flask , request,jsonify
import requests
from app import app
from functools import wraps

def user_decorator(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        user= requests.get('http://127.0.0.1:5001/user/current_user',headers= request.headers ).json()

        return f(user,*args,**kwargs)
    return decorated

@app.route('/login', methods=['GET','POST'])
def login():

    response = requests.get('http://127.0.0.1:5001/user/login', json=request.get_json())
    if response.status_code == 200:
        return response.json()
    return {'msg':'Login Failed'}

@app.post('/register/user')
def register_user():
    response = requests.post('http://127.0.0.1:5001/user/register', json=request.get_json())
    if response.status_code == 200:
        return {'msg':"user Added"},200
    return {"msg":"some error occure"},404

@app.get('/get_user')
def get_user():

    user= requests.get('http://127.0.0.1:5001/user/current_user',headers= request.headers )

    return user.json()

@app.get('/show_products')
@user_decorator
def show_products(user):
    if 'message' in user:
        return user
    
    all_products= requests.get('http://127.0.0.1:5002/product/all').json()
    return jsonify(all_products)

@app.post('/add_product')
@user_decorator
def add_product(user):
    if 'message' in user:
        return user
    
    if not user['admin']:
        return {'msg':'You can not add Products'}
    print(request.get_json())
    add_product= requests.post('http://127.0.0.1:5002/product/add', json=request.get_json()) 

    return add_product.json()


@app.get('/filter_product')
@user_decorator
def filter_product(user):
    if 'message' in user:
        return user
    
    product_filter= requests.get('http://127.0.0.1:5002/product/with_filter', json=request.get_json()) 

    return jsonify( product_filter.json())

@app.get('/view_cart')
@user_decorator
def view_cart(user):
    if 'message' in user:
        return user
    
    cart= requests.get('http://127.0.0.1:5003/order/view_cart/'+str(user['id'])).json()

    return jsonify(cart )

@app.get('/view_orders')
@user_decorator
def view_orders(user):
    if 'message' in user:
        return user
    
    orders= requests.get('http://127.0.0.1:5003/order/view_orders/'+str(user['id'])).json()

    return jsonify(orders )

@app.post('/add_to_cart')
@user_decorator
def add_to_cart(user):
    if 'message' in user:
        return user
    
    add_to_cart= requests.post('http://127.0.0.1:5003/order/add_to_cart/'+str(user['id']), json=request.get_json()).json()

    return jsonify(add_to_cart)

@app.post('/apply_coupon/<int:cart_id>')
@user_decorator
def apply_coupon(user,cart_id):
    if 'message' in user:
        return user
    
    apply_coupon= requests.post('http://127.0.0.1:5003/order/apply_coupon/'+str(cart_id)+'/'+str(user['id']), json=request.get_json()).json()

    return jsonify(apply_coupon)

@app.post('/place_order/<int:cart_id>')
@user_decorator
def place_order(user,cart_id):
    if 'message' in user:
        return user
    
    place_order= requests.post('http://127.0.0.1:5003/order/place_order/'+str(cart_id)+'/'+str(user['id'])).json()

    return jsonify(place_order)
