from unicodedata import category
from app import db

class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    category = db.Column(db.String(50))
    review = db.Column(db.Integer)
    price = db.Column(db.Integer)
    quantity= db.Column(db.Integer)
    discount_percentage= db.Column(db.Integer)
    discount_at_quantity= db.Column(db.Integer)

     
    def __init__(self, name, category, review, price, discount_percentage, discount_at_quantity, quantity):
        self.name= name 
        self.category= category
        self.review= review
        self.price= price
        self.discount_percentage= discount_percentage
        self.discount_at_quantity= discount_at_quantity
        self.quantity= quantity