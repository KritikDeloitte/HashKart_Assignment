import json
import logging
import unittest
import requests
from jsonschema import validate
import schema_helper as helper



class TestAPI(unittest.TestCase):
    TOKEN= ''
    def __init__(self, methodName: str = ...) :
        super().__init__(methodName)
        # res= requests.get(self.URL+'login',json=user)
        # self.TOKEN= res.json()['token']
    URL = 'http://127.0.0.1:5002/product/'
 

    def test_01_show_all_products(self):
        resp= requests.get(self.URL+'all')
        self.assertEqual(resp.status_code, 200)

    @unittest.SkipTest
    def test_02_add_product_200(self):

        resp= requests.post(self.URL+'add',json=helper.product_add_json)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()['msg'], 'Product added')
    
    def test_03_get_product_byId(self):
        resp= requests.get(self.URL+'get_product/'+str(2))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()['name'],"Redmi Note 10" )
        self.assertEqual(resp.json()['product_id'], 2)

    def test_04_get_product_byId_fail(self):
        resp= requests.get(self.URL+'get_product/'+str(0))
        self.assertEqual(resp.status_code, 404)
        self.assertEqual(resp.json()['msg'],"Product not available" )

    def test_05_product_quant_dec(self):
        resp= requests.get(self.URL+'dec_product/'+str(1)+'/'+str(1))
        self.assertEqual(resp.status_code, 200)

    def test_05_product_quant_dec_fail(self):
        resp= requests.get(self.URL+'dec_product/'+str(1000)+'/'+str(1))
        self.assertEqual(resp.status_code, 500)
    
    def test_06_product_filter_by_price(self):
        resp= requests.get(self.URL+'with_filter',json=helper.product_filter_by_category_json)
        self.assertEqual(resp.status_code, 200)

    
    def test_07_product_filter_by_price(self):
        resp= requests.get(self.URL+'with_filter',json=helper.product_filter_by_price_json)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()),2)

    def test_08_product_filter_by_price(self):
        resp= requests.get(self.URL+'with_filter',json=helper.product_filter_by_review_json)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()),4)

    def test_09_product_filter_by_price(self):
        resp= requests.get(self.URL+'with_filter',json=helper.product_filter_by_pirce_review_json)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()),2)
    
    def test_10_product_filter_empty(self):
        resp= requests.get(self.URL+'with_filter',json=helper.product_filter_by_category_json1)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()),0)

if __name__ == "__main__":
    unittest.main()
