from asyncio.windows_events import NULL
from email.policy import default
from re import S
from app import db

class Cart(db.Model):
    cart_id = db.Column(db.Integer, primary_key=True)
    product_id= db.Column(db.Integer)
    user_id= db.Column(db.Integer)
    name = db.Column(db.String(50))
    category = db.Column(db.String(50))
    price_of_product = db.Column(db.Integer)
    quantity= db.Column(db.Integer)
    total_amount_without_discount= db.Column(db.Integer)
    total_price_after_discount= db.Column(db.Integer)
    coupon_id= db.Column(db.Integer , nullable=True ,default= NULL)
    status= db.Column(db.Integer, default= 0)
    coupon_discount= db.Column(db.Integer, default= 0)
     
    def __init__(self, total_amount_without_discount, product_id ,user_id,name, category, price_of_product,  quantity, total_price_after_discount,status=0,coupon_discount=0,coupon_id=NULL):
        self.name= name 
        self.category= category
        self.coupon_id= coupon_id
        self.price_of_product= price_of_product
        self.product_id= product_id
        self.user_id= user_id
        self.total_price_after_discount= total_price_after_discount
        self.quantity= quantity
        self.status= status
        self.coupon_discount= coupon_discount
        self.total_amount_without_discount= total_amount_without_discount


class Coupon(db.Model):
    coupon_id= db.Column(db.Integer, primary_key=True)
    coupon_code= db.Column(db.String(50))
    discount_per= db.Column(db.Integer)
    status= db.Column(db.Boolean)

    def __init__(self, coupon_code, discount_per, status) :
        self.coupon_code= coupon_code
        self.discount_per= discount_per
        self.status= status



'''
        "name", "category", "coupon_id", "price_of_product", "product_id", "user_id", "total_price_after_discount", "discount_percentage", "discount_at_quantity", "quantity", "status", "coupon_discount"
'''