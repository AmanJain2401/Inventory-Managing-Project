from django.test import SimpleTestCase
from django.urls import resolve, reverse
from dashboard.views import index, staff, product, product_delete, product_update, order

class TestUrls(SimpleTestCase):

 def test_index_url_is_resolved(self):
    url = reverse('dashboard-index')
    self.assertEquals(resolve(url).func, index)

 def test_staff_url_is_resolved(self):
    url = reverse('dashboard-staff')
    self.assertEquals(resolve(url).func, staff)

def test_product_url_is_resolved(self):
    url = reverse('dashboard-product')
    self.assertEquals(resolve(url).func, product)

def test_order_url_is_resolved(self):
    url = reverse('dashboard-order')
    self.assertEquals(resolve(url).func, order)

def test_product_delete_url_is_resolved(self):
    url = reverse('dashboard-product-delete')
    self.assertEquals(resolve(url).func, product_delete)

def test_product_update_url_is_resolved(self):
    url = reverse('dashboard-product-update')
    self.assertEquals(resolve(url).func, product_update)