import unittest
import time
from unittest.mock import MagicMock
from pynput.keyboard import Controller
from src.input.key_operator import KeyOperator
from tests.support.test_util import TestUtil

class TestKeyOperator(unittest.TestCase):
    def setUp(self):
        self.key_operator = KeyOperator()
        self.test_util = TestUtil()
        self.original_keyboard_press = Controller.press
        self.original_keyboard_release = Controller.release
        self.original_sleep = time.sleep
        Controller.press = MagicMock(name="test_defined_key__keyboard_press")
        Controller.release = MagicMock(name="test_defined_key__keyboard_save")
        time.sleep = MagicMock(name="test_defined_key__sleep")

    def tearDown(self):
        Controller.press = self.original_keyboard_press
        Controller.release = self.original_keyboard_release
        time.sleep = self.original_sleep

    def test_press_keys(self):
        self.key_operator.press_keys(['a', 'b'])
        self.test_util.assert_called_with_args_x_times(Controller.press, ['a'], 1)
        self.test_util.assert_called_with_args_x_times(Controller.press, ['b'], 1)

    def test_release_keys(self):
        self.key_operator.release_keys(['a', 'b'])
        self.test_util.assert_called_with_args_x_times(Controller.release, ['a'], 1)
        self.test_util.assert_called_with_args_x_times(Controller.release, ['b'], 1)

    def test_press_keys_without_holding(self):
        self.key_operator.press_keys_without_holding(['a', 'b'])
        self.test_util.assert_called_with_args_x_times(Controller.press, ['a'], 1)
        self.test_util.assert_called_with_args_x_times(Controller.press, ['b'], 1)
        time.sleep.assert_not_called()
        self.test_util.assert_called_with_args_x_times(Controller.release, ['a'], 1)
        self.test_util.assert_called_with_args_x_times(Controller.release, ['b'], 1)
        
    def test_press_and_hold_keys(self):
        self.key_operator.press_and_hold_keys(['a', 'b'], 5)
        self.test_util.assert_called_with_args_x_times(Controller.press, ['a'], 1)
        self.test_util.assert_called_with_args_x_times(Controller.press, ['b'], 1)
        self.test_util.assert_called_with_args_x_times(time.sleep, [5], 1)
        self.test_util.assert_called_with_args_x_times(Controller.release, ['a'], 1)
        self.test_util.assert_called_with_args_x_times(Controller.release, ['b'], 1)
