import json


view_cart_user_1 =     {
        "cart_id": 4,
        "category": "Book",
        "coupon_discount": 140,
        "coupon_id": 5,
        "name": "My Book",
        "price_of_product": 140,
        "product_id": 12,
        "quantity": 2,
        "status": 0,
        "total_price_after_discount": 140,
        "user_id": 1
    }

add_to_cart_string= '{"quantity_to_buy":1, "product_id": 4}'

add_to_cart_json= json.loads(add_to_cart_string)

add_to_cart_string_fail= '{"quantity_to_buy":1, "product_id": 1234}'

add_to_cart_json_fail= json.loads(add_to_cart_string_fail)

apply_coupon_string='{"coupon_code" : "kritik50"}'

apply_coupon_json= json.loads(apply_coupon_string)


apply_coupon_string_fail='{"coupon_code" : "u20"}'

apply_coupon_json_fail= json.loads(apply_coupon_string_fail)

add_coupon_card_string=  '{ "coupon_code" : "mobile5","discount_per" : 5}'

add_coupon_card_json = json.loads(add_coupon_card_string)
