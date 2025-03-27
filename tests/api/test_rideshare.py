# import unittest
# from tests.test_utils import *

# class Test(unittest.TestCase):
    
#     def test_create_driver(self):
#         data = {
#             'name': 'name',
#             'average_rating': 5.0,
#             'special_instructions': 'special_instructions',
#             'car_make_model': 'car_make_model',
#             'license_number': 'license_number',
#             'years_as_driver': 10,
#             'joining_date': '2024-01-01',
#             'coordinates': '40.0000, 40.0000',
#             'zipcode': 'zipcode'
#         }
#         actual_1 = post_rest_call_200(self, 'http://localhost:5000/drivers', data)
#         self.assertIsNotNone(actual_1.get('driver_id'), 'should be 6')
#         id = actual_1['driver_id']
#         actual_2 = get_rest_call_200(self, f'http://localhost:5000/driver/{id}')
#         self.assertEqual(len(actual_2), 1, 'should be 1')

#     def test_create_rider(self):
#         data = {
#             'name': 'name',
#             'average_rating': 5.0,
#             'special_instructions': 'special_instructions',
#             'credit_card_number': 'credit_card_number',
#             'used_for': 'used_for',
#             'years_as_rider': 10,
#             'joining_date': '2024-01-01',
#             'coordinates': '40.0000, 40.0000',
#             'zipcode': 'zipcode'
#         }
#         actual_1 = post_rest_call_200(self, 'http://localhost:5000/riders', data)
#         self.assertIsNotNone(actual_1.get('rider_id'), 'should be 6')
#         id = actual_1['rider_id']
#         actual_2 = get_rest_call_200(self, f'http://localhost:5000/rider/{id}')
#         self.assertEqual(len(actual_2), 1, 'should be 1')

#     def test_create_ride(self):
#         data = {
#             'driver_id': 1,
#             'rider_id': 1,
#             'start_point': 'start_point',
#             'destination': 'destination',
#             'special_instructions': 'special_instructions',
#             'time_info': '2024-01-01 00:00:00',
#             'driver_review_text': 'driver_review_text',
#             'rider_review_text': 'rider_review_text',
#             'done': False
#         }
#         actual_1 = post_rest_call_200(self, 'http://localhost:5000/rides', data)
#         self.assertIsNotNone(actual_1.get('ride_id'), 'should be 6')
#         id = actual_1['ride_id']
#         actual_2 = get_rest_call_200(self, f'http://localhost:5000/ride/{id}')
#         self.assertEqual(len(actual_2), 1, 'should be 1')

#     def test_create_review(self):
#         data = {
#             'ride_id': 1,
#             'reviewer_id': 1,
#             'review_text': 'review_text',
#             'done': False
#         }
#         actual_1 = post_rest_call_200(self, 'http://localhost:5000/reviews', data)
#         self.assertIsNotNone(actual_1.get('review_id'), 'should be 6')
#         id = actual_1['review_id']
#         actual_2 = get_rest_call_200(self, f'http://localhost:5000/review/{id}')
#         self.assertEqual(len(actual_2), 1, 'should be 1')

#     def test_read_home(self):
#         post_rest_call_200(self, 'http://localhost:5000/manage/init')
#         actual = get_rest_call_200(self, 'http://localhost:5000/')
#         self.assertEqual(actual['message'], 'rideshare', 'should be rideshare')
    
#     def test_read_drivers(self):
#         post_rest_call_200(self, 'http://localhost:5000/manage/init')
#         actual = get_rest_call_200(self, 'http://localhost:5000/drivers')
#         self.assertEqual(len(actual), 5, 'should be 5')
        
#     def test_read_riders(self):
#         post_rest_call_200(self, 'http://localhost:5000/manage/init')
#         actual = get_rest_call_200(self, 'http://localhost:5000/riders')
#         self.assertEqual(len(actual), 5, 'should be 5')

#     def test_read_rides(self):
#         post_rest_call_200(self, 'http://localhost:5000/manage/init')
#         actual = get_rest_call_200(self, 'http://localhost:5000/rides')
#         self.assertEqual(len(actual), 5, 'should be 5')

#     def test_read_reviews(self):
#         post_rest_call_200(self, 'http://localhost:5000/manage/init')
#         actual = get_rest_call_200(self, 'http://localhost:5000/reviews')
#         self.assertEqual(len(actual), 5, 'should be 5')
        
#     def test_read_nonexistent_driver(self):
#         post_rest_call_200(self, 'http://localhost:5000/manage/init')
#         actual = get_rest_call_404(self, 'http://localhost:5000/driver/6')
#         self.assertEqual(actual['message'], 'driver is not found', 'should be driver is not found')
        
#     def test_read_nonexistent_rider(self):
#         post_rest_call_200(self, 'http://localhost:5000/manage/init')
#         actual = get_rest_call_404(self, 'http://localhost:5000/rider/6')
#         self.assertEqual(actual['message'], 'rider is not found', 'should be rider is not found')
    
#     def test_read_nonexistent_ride(self):
#         post_rest_call_200(self, 'http://localhost:5000/manage/init')
#         actual = get_rest_call_404(self, 'http://localhost:5000/ride/6')
#         self.assertEqual(actual['message'], 'ride is not found', 'should be ride is not found')
        
#     def test_read_nonexistent_review(self):
#         post_rest_call_200(self, 'http://localhost:5000/manage/init')
#         actual = get_rest_call_404(self, 'http://localhost:5000/review/6')
#         self.assertEqual(actual['message'], 'review is not found', 'should be review is not found')

#     def test_read_driver(self):
#         post_rest_call_200(self, 'http://localhost:5000/manage/init')
#         actual = get_rest_call_200(self, f'http://localhost:5000/driver/1')
#         self.assertEqual(len(actual), 10, 'should be 10')

#     def test_read_rider(self):
#         post_rest_call_200(self, 'http://localhost:5000/manage/init')
#         actual = get_rest_call_200(self, f'http://localhost:5000/rider/1')
#         self.assertEqual(len(actual), 10, 'should be 10')

#     def test_read_ride(self):
#         post_rest_call_200(self, 'http://localhost:5000/manage/init')
#         actual = get_rest_call_200(self, f'http://localhost:5000/ride/1')
#         self.assertEqual(len(actual), 10, 'should be 10')

#     def test_read_review(self):
#         post_rest_call_200(self, 'http://localhost:5000/manage/init')
#         actual = get_rest_call_200(self, f'http://localhost:5000/review/1')
#         self.assertEqual(len(actual), 5, 'should be 5')
        
#     def test_update_driver(self):
#         post_rest_call_200(self, 'http://localhost:5000/manage/init')
#         data = {
#             'name': 'updated name',
#             'average_rating': 5.0,
#             'special_instructions': 'updated special instructions',
#             'car_make_model': 'updated car make model',
#             'license_number': 'updated license number',
#             'years_as_driver': 10,
#             'joining_date': '2024-01-01',
#             'coordinates': '40.0000, 40.0000',
#             'zipcode': 'updated zipcode'
#         }
#         actual_1 = put_rest_call_200(self, f'http://localhost:5000/driver/1', data)
#         self.assertEqual(actual_1['driver_id'], 1, 'should be 1')
#         self.assertEqual(actual_1['message'], 'driver is updated', 'should be driver is updated')
#         actual_2 = get_rest_call_200(self, f'http://localhost:5000/driver/1')
#         self.assertEqual(actual_2['name'], 'updated name', 'should be updated name')
    
#     def test_update_rider(self):
#         post_rest_call_200(self, 'http://localhost:5000/manage/init')
#         data = {
#             'name': 'updated name',
#             'average_rating': 5.0,
#             'special_instructions': 'updated special instructions',
#             'credit_card_number': 'updated credit card number',
#             'used_for': 'updated used for',
#             'years_as_rider': 10,
#             'joining_date': '2024-01-01',
#             'coordinates': '40.0000, 40.0000',
#             'zipcode': 'updated zipcode'
#         }
#         actual_1 = put_rest_call_200(self, f'http://localhost:5000/rider/1', data)
#         self.assertEqual(actual_1['rider_id'], 1, 'should be 1')
#         self.assertEqual(actual_1['message'], 'rider is updated', 'should be rider is updated')
#         actual_2 = get_rest_call_200(self, f'http://localhost:5000/rider/1')
#         self.assertEqual(actual_2['name'], 'updated name', 'should be updated name')
    
#     def test_update_ride(self):
#         post_rest_call_200(self, 'http://localhost:5000/manage/init')
#         data = {
#             'driver_id': 1,
#             'rider_id': 1,
#             'start_point': 'updated start point',
#             'destination': 'updated destination',
#             'special_instructions': 'updated special instructions',
#             'time_info': '2024-01-01 00:00:00',
#             'driver_review_text': 'updated driver review text',
#             'rider_review_text': 'updated rider review text',
#             'done': True
#         }
#         actual_1 = put_rest_call_200(self, f'http://localhost:5000/ride/1', data)
#         self.assertEqual(actual_1['ride_id'], 1, 'should be 1')
#         self.assertEqual(actual_1['message'], 'ride is updated', 'should be ride is updated')
#         actual_2 = get_rest_call_200(self, f'http://localhost:5000/ride/1')
#         self.assertEqual(actual_2['done'], True, 'should be true')

#     def test_update_review(self):
#         post_rest_call_200(self, 'http://localhost:5000/manage/init')
#         data = {
#             'ride_id': 1,
#             'reviewer_id': 1,
#             'review_text': 'updated review text',
#             'done': True
#         }
#         actual_1 = put_rest_call_200(self, f'http://localhost:5000/review/1', data)
#         self.assertEqual(actual_1['review_id'], 1, 'should be 1')
#         self.assertEqual(actual_1['message'], 'review is updated', 'should be review is updated')
#         actual_2 = get_rest_call_200(self, f'http://localhost:5000/review/1')
#         self.assertEqual(actual_2['done'], True, 'should be true')

#     def test_delete_driver(self):
#         post_rest_call_200(self, 'http://localhost:5000/manage/init')
#         actual_1 = delete_rest_call_200(self, f'http://localhost:5000/driver/1')
#         self.assertEqual(actual_1['message'], 'driver is deleted', 'should be driver is deleted')
#         actual_2 = get_rest_call_404(self, f'http://localhost:5000/driver/1')
#         self.assertEqual(actual_2['message'], 'driver is not found', 'should be driver is not found')

#     def test_delete_rider(self):
#         post_rest_call_200(self, 'http://localhost:5000/manage/init')
#         actual_1 = delete_rest_call_200(self, f'http://localhost:5000/rider/1')
#         self.assertEqual(actual_1['message'], 'rider is deleted', 'should be rider is deleted')
#         actual_2 = get_rest_call_404(self, f'http://localhost:5000/rider/1')
#         self.assertEqual(actual_2['message'], 'rider is not found', 'should be rider is not found')

#     def test_delete_ride(self):
#         post_rest_call_200(self, 'http://localhost:5000/manage/init')
#         actual_1 = delete_rest_call_200(self, f'http://localhost:5000/ride/1')
#         self.assertEqual(actual_1['message'], 'ride is deleted', 'should be ride is deleted')
#         actual_2 = get_rest_call_404(self, f'http://localhost:5000/ride/1')
#         self.assertEqual(actual_2['message'], 'ride is not found', 'should be ride is not found')

#     def test_delete_review(self):
#         post_rest_call_200(self, 'http://localhost:5000/manage/init')
#         actual_1 = delete_rest_call_200(self, f'http://localhost:5000/review/1')
#         self.assertEqual(actual_1['message'], 'review is deleted', 'should be review is deleted')
#         actual_2 = get_rest_call_404(self, f'http://localhost:5000/review/1')
#         self.assertEqual(actual_2['message'], 'review is not found', 'should be review is not found')