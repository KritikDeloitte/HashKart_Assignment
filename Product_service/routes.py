from pickle import NONE
from unicodedata import category
from urllib import request
from app import app,db,ma
from model  import Product
from flask import request, jsonify
import helper_functions

class ProductSchema(ma.Schema):
    class Meta:
        fields = ("product_id", "name", "category", "price" ,"quantity","review","discount_at_quantity","discount_percentage")

product_schema= ProductSchema()
products_schema= ProductSchema(many=True)


@app.route('/product/all',methods=['GET'])
def get_all_products():
    response= Product.query.all()
    return jsonify(products_schema.dump(response))

@app.route('/product/add',methods=['POST'])
def add_product():
    data= request.get_json()
    new_product= Product(name= data['name'],category= data['category'], price= data['price'], quantity= data['quantity'], review= data['review'], discount_at_quantity= data['discount_at_quantity'], discount_percentage= data['discount_percentage'])
    db.session.add(new_product)
    db.session.commit()
    return {'msg':'Product added'}

@app.get('/product/with_filter')
def show_product_with_filter():
    data= request.get_json()
    response= []
    result=  Product.query.filter_by(category= data['category']).all()
 
    if 'category' in data and 'start_price'  in data and 'review_above' in data:
        response= helper_functions.sort_price_review(products= result , data=data)
        print('a')
    elif 'category' in data and 'start_price' in data:
        print('b')
        response= helper_functions.sort_price(products= result, data= data)
    elif 'category' in data and 'review_above' in data:
        print('c')
        response= helper_functions.sort_rating(products= result, data= data)
    else:

        response= helper_functions.sort_category(products= result)
    return jsonify(response)


@app.get('/product/get_product/<int:product_id>')
def get_procut_with_id(product_id):
    product= Product.query.filter_by(product_id= product_id).first()
    if not product:
        return {'msg':'Product not available'} , 404
    return jsonify( product_schema.dump(product))

@app.get('/product/dec_product/<int:product_id>/<int:quant_to_dec>')
def dec_product(product_id,quant_to_dec):
    product= Product.query.filter_by(product_id= product_id).first()
    
    product.quantity -= quant_to_dec
    try:
        db.session.commit()
    except:
        return {"msg":"error happen "}
    return {
        "msg": "complete"
    }