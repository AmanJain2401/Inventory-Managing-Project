from pydoc import cli
from urllib import response
from django.test import TestCase, client
from django.urls import reverse
from dashboard.models import product, order, CATEGORY
import json

class TestViews(TestCase):
    
    def setUp(self):
        self.client=client()
        self.product_url=reverse('dashboard-product')
        self.order_url=reverse('dashboard-order')
    
    def test_product_GET(self):
        response= self.client.get( self.product_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/product.html')
    
    def test_order_GET(self):
        response= self.client.get( self.order_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/order.html')
