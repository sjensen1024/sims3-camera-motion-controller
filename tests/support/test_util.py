import unittest
from unittest.mock import call

class TestUtil(unittest.TestCase):
   def assert_called_with_args_x_times(self, method_called, arguments, number_of_times):
      self.assertEqual(method_called.call_args_list.count(call(*arguments)), number_of_times)
