import json
product_add_string=  '{"name": "Banana - 1 dozen","category": "Grocery","review": 6,"price": 40,"discount_percentage": 5,"discount_at_quantity": 5,"quantity": 50}'

product_add_json= json.loads(
    product_add_string
    )

product_filter_by_price_string= '{"category":"Grocery", "start_price":100,"end_price":180}'

product_filter_by_price_json= json.loads(product_filter_by_price_string)

product_filter_by_review_string= '{"category":"Grocery", "review_above":3}'


product_filter_by_review_json= json.loads(product_filter_by_review_string)

product_filter_by_pirce_review_string= '{"category":"Grocery", "review_above":3,"start_price":100,"end_price":180}'


product_filter_by_pirce_review_json= json.loads(product_filter_by_pirce_review_string)

product_filter_by_category_string= '{"category":"Grocery"}'


product_filter_by_category_json= json.loads(product_filter_by_category_string)

product_filter_by_category_string1= '{"category":"Headphone"}'


product_filter_by_category_json1= json.loads(product_filter_by_category_string1)