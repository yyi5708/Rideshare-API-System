# import unittest
# from tests.test_utils import *

# class TestDBSchema(unittest.TestCase):

#     def test_rebuild_tables(self):
#         post_rest_call(self, 'http://localhost:5000/manage/init')
#         count = get_rest_call(self, 'http://localhost:5000')
#         self.assertEqual(len(count), 1)

#     def test_rebuild_tables_is_idempotent(self):
#         post_rest_call(self, 'http://localhost:5000/manage/init')
#         post_rest_call(self, 'http://localhost:5000/manage/init')
#         count = get_rest_call(self, 'http://localhost:5000')
#         self.assertEqual(len(count), 1)