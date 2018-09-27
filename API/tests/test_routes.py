from ..app import api
import unittest
import json

class All_tests(unittest.TestCase):

    def setUp(self):
        self.my_test = api.test_client(self)
        self.sample_data = {
            'by':'sample_user',
            'order':'fries only',
            'status':'pending'
        }
        self.empty = dict()
        self.any_data = dict()
        self.updater = {
            'status':'done'
        }
        self.incomplete = {
	            "by":"sample user",
	            "status":"pending",
                }
        self.done = {
            'by':'sample_user',
            'order':'fries only',
            'status':'done'
        }
            
        
      
      
    def test_index(self):
        feedback = self.my_test.get('/api/v1/', content_type='application/json')
        self.assertNotEqual(feedback.status_code, 404)

    def test_defualt_route_returns_correct_info(self):
        response = self.my_test.get('/api/v1/', content_type='application/json')
        self.assertTrue(b'WELCOME TO FAST FOODS FAST' in response.data)

    def test_post_method_invalid_input(self):
        response = self.my_test.post('api/v1/post/orders', data=json.dumps(self.sample_data), content_type='text/plain')
        self.assertTrue(b'TypeError', response.data)


    def test_missing_values_in_post_method(self):
        response = self.my_test.post('api/v1/post/orders', data=json.dumps(self.incomplete), content_type='application/json')
        self.assertTrue(b'KeyErrr', response.data)

    def test_for_post_method_working(self):
        response = self.my_test.post('/api/v1/post/orders', data= json.dumps(self.sample_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_order_really_created(self):
        response = self.my_test.post('/api/v1/post/orders', data= json.dumps(self.sample_data), content_type='application/json')
        self.assertTrue(response.status_code, 200)

    def test_empty_order_not_accepted(self):
        response = self.my_test.post('/api/v1/post/orders', data= json.dumps(self.empty), content_type='application/json')
        self.assertTrue(response.status_code, 500)
        #error code 500 server cannot process therequest for an unknown reason.

    def test_get_all_endpoint(self):
        responce = self.my_test.get('/api/v1/get/orders', content_type='application/json')
        self.assertEqual(responce.status_code, 200)

    def test_get_order_with_wrong_id(self):
        response = self.my_test.post('/api/v1/post/orders', data= json.dumps(self.sample_data), content_type='application/json')
        response = self.my_test.get('api/v1/get/orders/5', content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'error', response.data)
        
    def test_update(self):
        response = self.my_test.post('/api/v1/post/orders', data= json.dumps(self.sample_data), content_type='application/json')
        response = self.my_test.put('/api/v1/get/orders/1', data=json.dumps(self.updater), content_type='application/json')
        self.assertTrue(b'The update was successfull' in response.data)

    def test_delete_cant_delete_data_not_existing(self):
        response = self.my_test.post('/api/v1/post/orders', data= json.dumps(self.sample_data), content_type='application/json')
        response = self.my_test.delete('/api/v1/order/5', content_type='application/json')
        self.assertIn(b'error', response.data)
        self.assertTrue(response.status_code, 200)

    def test_delete_works(self):
        response = self.my_test.post('/api/v1/post/orders', data= json.dumps(self.sample_data), content_type='application/json')
        response = self.my_test.delete('/api/v1/order/2', content_type='application/json')
        self.assertIn(b'order deleted', response.data)

    def test_cannot_update_done_order(self):
        response = self.my_test.post('/api/v1/post/orders', data= json.dumps(self.done), content_type='application/json')
        response = self.my_test.put('/api/v1/get/orders/2', data=json.dumps(self.updater), content_type='application/json')
        self.assertIn(b'Somethong Went wrong!', response.data)

