import json
import logging
import unittest
import requests
import cart_test_helper as helper


class TestAPI(unittest.TestCase):
    TOKEN= ''
    def __init__(self, methodName: str = ...) :
        super().__init__(methodName)
        # res= requests.get(self.URL+'login',json=user)
        # self.TOKEN= res.json()['token']
    URL = 'http://127.0.0.1:5003/order/'
 

    def test_01_view_cart(self):
        resp= requests.get(self.URL+'view_cart/'+str(1))
        self.assertEqual(resp.status_code, 200)
        self.assertDictEqual(resp.json()[0],helper.view_cart_user_1)

    def test_02_view_order(self):

        resp= requests.get(self.URL+'view_orders/'+str(1))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 3)
    
    def test_03_view_cart_empty(self):
        resp= requests.get(self.URL+'view_cart/'+str(1000))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 0)

    @unittest.skip
    def test_04_add_to_cart(self):
        resp= requests.post(self.URL+'add_to_cart/'+str(2),json=helper.add_to_cart_json)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()['msg'],"Product added to Cart" )
    
    def test_05_add_to_cart_fail(self):
        resp= requests.post(self.URL+'add_to_cart/'+str(1),json=helper.add_to_cart_json_fail)
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(resp.json()['msg'],"Product not available" )
    
    @unittest.skip
    def test_06_apply_coupon(self):
        resp= requests.post(self.URL+'apply_coupon/'+str(8)+'/'+str(2),json=helper.apply_coupon_json)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()['msg'],"Coupon Applied" )
    
    def test_07_apply_coupon_fail(self):
        resp= requests.post(self.URL+'apply_coupon/'+str(8)+'/'+str(2),json=helper.apply_coupon_json_fail)
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(resp.json()['msg'],"Coupon invalid" )
    
    @unittest.skip
    def test_08_place_order(self):
        resp= requests.post(self.URL+'place_order/'+str(10)+'/'+str(2))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()['msg'],"Product added to order" )

    def test_09_place_order_fail_1(self):
        resp= requests.post(self.URL+'place_order/'+str(9)+'/'+str(2))
        self.assertEqual(resp.status_code, 405)
        self.assertEqual(resp.json()['msg'],"Product Qantity not available" )
        

    def test_10_place_order_fail_2(self):
        resp= requests.post(self.URL+'place_order/'+str(100)+'/'+str(2))
        self.assertEqual(resp.status_code, 404)
        self.assertEqual(resp.json()['msg'],"Invaild cart id" )
    
    def test_10_place_order_fail_3(self):
        resp= requests.post(self.URL+'place_order/'+str(9)+'/'+str(1000))
        self.assertEqual(resp.status_code, 403)
        self.assertEqual(resp.json()['msg'],"You are not owner of this cart" )

    @unittest.skip
    def test_11_add_coupon_card(self):
        resp= requests.post(self.URL+'add_coupon_card',json=helper.add_coupon_card_json )
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()['msg'],"coupon added" )
    





    

    # def test_05_product_quant_dec(self):
    #     resp= requests.get(self.URL+'dec_product/'+str(1)+'/'+str(1))
    #     self.assertEqual(resp.status_code, 200)

    # def test_05_product_quant_dec_fail(self):
    #     resp= requests.get(self.URL+'dec_product/'+str(1000)+'/'+str(1))
    #     self.assertEqual(resp.status_code, 500)
    
    # def test_06_product_filter_by_price(self):
    #     resp= requests.get(self.URL+'with_filter',json=helper.product_filter_by_category_json)
    #     self.assertEqual(resp.status_code, 200)

    
    # def test_07_product_filter_by_price(self):
    #     resp= requests.get(self.URL+'with_filter',json=helper.product_filter_by_price_json)
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertEqual(len(resp.json()),2)

    # def test_08_product_filter_by_price(self):
    #     resp= requests.get(self.URL+'with_filter',json=helper.product_filter_by_review_json)
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertEqual(len(resp.json()),4)

    # def test_09_product_filter_by_price(self):
    #     resp= requests.get(self.URL+'with_filter',json=helper.product_filter_by_pirce_review_json)
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertEqual(len(resp.json()),2)
    
    # def test_10_product_filter_empty(self):
    #     resp= requests.get(self.URL+'with_filter',json=helper.product_filter_by_category_json1)
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertEqual(len(resp.json()),0)

if __name__ == "__main__":
    unittest.main()
