
def sort_price_review(products , data):
    sorted_data= []
    for i in products:
        if i.price >= data['start_price'] and i.price <= data['end_price'] and i.review >= data['review_above']:
            product_data= {}
            product_data['name']= i.name
            product_data['review']= i.review
            product_data['price']= i.price
            product_data['discount_percentage']= i.discount_percentage
            product_data['discount_at_quantity']= i.discount_at_quantity
            product_data['quantity']= i.quantity
            sorted_data.append(product_data)
    return sorted_data

def sort_price(products, data):
    sorted_data= []
    for i in products:
        if i.price >= data['start_price'] and i.price <= data['end_price']:
            product_data= {}
            product_data['name']= i.name
            product_data['review']= i.review
            product_data['price']= i.price
            product_data['discount_percentage']= i.discount_percentage
            product_data['discount_at_quantity']= i.discount_at_quantity
            product_data['quantity']= i.quantity
            sorted_data.append(product_data)
    return sorted_data

def sort_rating(products , data):
    sorted_data= []
    for i in products:
        if i.review >= data['review_above']:
            product_data= {}
            product_data['name']= i.name
            product_data['review']= i.review
            product_data['price']= i.price
            product_data['discount_percentage']= i.discount_percentage
            product_data['discount_at_quantity']= i.discount_at_quantity
            product_data['quantity']= i.quantity
            sorted_data.append(product_data)
    return sorted_data

def sort_category(products ):
    sorted_data= []
    for i in products:
        product_data= {}
        product_data['name']= i.name
        product_data['review']= i.review
        product_data['price']= i.price
        product_data['discount_percentage']= i.discount_percentage
        product_data['discount_at_quantity']= i.discount_at_quantity
        product_data['quantity']= i.quantity
        sorted_data.append(product_data)
    return sorted_data
