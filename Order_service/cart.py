import json
from flask import request, jsonify
from app import app , ma ,db
from model import Cart, Coupon
import requests


class CartSchema(ma.Schema):
    class Meta:
        fields = ("cart_id","name", "category", "coupon_id", "price_of_product", "product_id", "user_id", "total_price_after_discount", "discount_percentage", "discount_at_quantity", "quantity", "status", "coupon_discount")

cart_schema= CartSchema()
carts_schema=CartSchema(many=True)

class CouponSchema(ma.Schema):
    class Meta:
        fields = ("coupon_id","coupon_code", "discount_per", "status")
coupon_schema= CouponSchema()
coupons_schema=CouponSchema(many=True)

@app.get('/order/view_cart/<int:user_id>')
def view_cart(user_id):
    cart_detail= Cart.query.filter_by(user_id= user_id, status= 0)

    return jsonify(carts_schema.dump(cart_detail))

@app.get('/order/view_orders/<int:user_id>')
def view_orders(user_id):
    order_details= Cart.query.filter_by(user_id= user_id, status= 1)
    return jsonify(carts_schema.dump(order_details))

@app.post('/order/add_to_cart/<int:user_id>')
def add_to_cart(user_id):
    product_detail= request.get_json()
    product= requests.get('http://127.0.0.1:5002/product/get_product/' + str(product_detail['product_id']))
    if product.status_code != 200:
        return {'msg':"Product not available"},400
    product_json= product.json()

    total_price= product_json['price'] * product_detail['quantity_to_buy']
    price_with_discount= total_price
    if(product_detail['quantity_to_buy'] >= product_json['discount_at_quantity']):
        price_with_discount-= int((total_price*product_json['discount_percentage'])/100)

    new_cart= Cart(category= product_json['category'] ,
                    name= product_json['name'],
                    price_of_product= product_json['price'],
                    quantity= product_detail['quantity_to_buy'],
                    total_amount_without_discount= total_price,
                    total_price_after_discount= price_with_discount,
                    product_id= product_detail['product_id'],
                    user_id= user_id)       
    db.session.add(new_cart)
    db.session.commit()
    return {'msg':'Product added to Cart'}


@app.post('/order/apply_coupon/<int:cart_id>/<int:user_id>')
def apply_coupon(cart_id,user_id):
    data= request.get_json()
    coupon= Coupon.query.filter_by(coupon_code= data['coupon_code']).first()
    if(coupon and coupon.status == True):
        
        cart= Cart.query.filter_by(cart_id= cart_id).first()
        if cart.status == 1:
            return {'msg':'Can not apply Coupon bcoz it has been ordered'},405
        if cart.user_id != user_id:
            return {"msg":"You are not owner of this cart"},401
        coupon_dis= int((cart.total_amount_without_discount* coupon.discount_per)/100)
        cart.coupon_id= coupon.coupon_id
        cart.coupon_discount= coupon_dis
        if cart.total_price_after_discount - coupon_dis <0:
            cart.total_price_after_discount=0
        else:
            cart.total_price_after_discount-= coupon_dis 
        db.session.commit()
        return {'msg':"Coupon Applied"}

    else:
        return {'msg': "Coupon invalid"},400


@app.post('/order/place_order/<int:cart_id>/<int:user_id>')
def place_order(cart_id,user_id):
    cart= Cart.query.filter_by(cart_id=cart_id , status= 0).first()
    if not cart:
        return {"msg":"Invaild cart id"},404
    if cart.user_id != user_id:
        return {"msg":"You are not owner of this cart"},403

    product= requests.get('http://127.0.0.1:5002/product/get_product/' + str(cart.product_id))
    product_json= product.json()
    if(product_json['quantity'] >=  cart.quantity):
        cart.status= 1
        if cart.coupon_id:
            coupon= Coupon.query.filter_by(coupon_id= cart.coupon_id).first()
            coupon.status= False
            db.session.commit()
        db.session.commit()
        product_dec= requests.get('http://127.0.0.1:5002/product/dec_product/' + str(cart.product_id) + '/' + str(cart.quantity))

    else:
        return {'msg': 'Product Qantity not available'},405
    return {'msg': 'Product added to order'}
    

@app.post('/order/add_coupon_card')
def add_coupon_card():
    data= request.get_json()
    new_coupon= Coupon(coupon_code= data['coupon_code'], discount_per= data['discount_per'], status=True)

    db.session.add(new_coupon)
    db.session.commit()
    return {"msg": "coupon added"}

@app.get('/order/get_all_coupon')
def get_all_coupon():
    coupons= Coupon.query.all()
    return jsonify(coupons_schema.dump(coupons))
