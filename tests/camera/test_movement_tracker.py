import unittest
from unittest.mock import MagicMock
from src.input.key_operator import KeyOperator
from src.input.key_set import KeySet
from tests.support.test_util import TestUtil
from src.camera.movement_tracker import MovementTracker

class TestMovementTracker(unittest.TestCase):
    def setUp(self):
        self.movement_tracker = MovementTracker()
        self.test_util = TestUtil()
        self.original_press_keys = KeyOperator.press_keys
        self.original_release_keys = KeyOperator.release_keys
        KeyOperator.press_keys = MagicMock("test_movement_tracker__press_keys")
        KeyOperator.release_keys = MagicMock("test_movement_tracker__release_keys")

    def tearDown(self):
        KeyOperator.press_keys = self.original_press_keys
        KeyOperator.release_keys = self.original_release_keys

    def test_when_init_given_checking_key_operator_then_should_be_not_none(self):
        self.assertIsNotNone(self.movement_tracker.key_operator)

    def test_when_init_given_checking_is_moving_forward_then_should_be_false(self):
        self.assertFalse(self.movement_tracker.is_moving_forward)

    def test_when_init_given_checking_is_moving_backward_then_should_be_false(self):
        self.assertFalse(self.movement_tracker.is_moving_backward)

    def test_when_init_given_checking_is_moving_left_then_should_be_false(self):
        self.assertFalse(self.movement_tracker.is_moving_left)

    def test_when_init_given_checking_is_moving_right_then_should_be_false(self):
        self.assertFalse(self.movement_tracker.is_moving_right)

    def test_when_init_given_checking_is_raising_then_should_be_false(self):
        self.assertFalse(self.movement_tracker.is_raising)

    def test_when_init_given_checking_is_lowering_then_should_be_false(self):
        self.assertFalse(self.movement_tracker.is_lowering)

    def test_when_init_given_checking_is_zooming_in_then_should_be_false(self):
        self.assertFalse(self.movement_tracker.is_zooming_in)

    def test_when_init_given_checking_is_zooming_out_then_should_be_false(self):
        self.assertFalse(self.movement_tracker.is_zooming_out)

    def test_when_init_given_checking_is_rotating_left_then_should_be_false(self):
        self.assertFalse(self.movement_tracker.is_rotating_left)

    def test_when_init_given_checking_is_rotating_right_then_should_be_false(self):
        self.assertFalse(self.movement_tracker.is_rotating_right)

    def test_when_init_given_checking_is_turning_left_then_should_be_false(self):
        self.assertFalse(self.movement_tracker.is_turning_left)

    def test_when_init_given_checking_is_turning_right_then_should_be_false(self):
        self.assertFalse(self.movement_tracker.is_turning_right)

    def test_when_start_moving_forward_given_is_not_already_moving_forward_then_should_start_moving_forward_and_stop_moving_backward(self):
        self.__test_start_movement_when_not_started_yet("start_moving_forward", "is_moving_forward", KeySet.MOVE_FORWARD.value, "stop_moving_backward")

    def test_when_start_moving_forward_given_is_already_moving_forward_then_should_keep_moving_forward_without_doing_anything_else(self):
        self.__test_start_movement_when_already_started("start_moving_forward", "is_moving_forward", "stop_moving_backward")

    def test_when_stop_moving_forward_given_is_moving_forward_then_should_stop_moving_forward(self):
        self.__test_stop_movement_when_started("stop_moving_forward", "is_moving_forward", KeySet.MOVE_FORWARD.value)

    def test_when_stop_moving_forward_given_is_not_moving_forward_yet_then_should_stay_not_moving_forward(self):
         self.__test_stop_movement_when_not_started_yet("stop_moving_forward", "is_moving_forward")

    def test_when_start_moving_backward_given_is_not_already_moving_backward_then_should_start_moving_backward_and_stop_moving_forward(self):
        self.__test_start_movement_when_not_started_yet("start_moving_backward", "is_moving_backward", KeySet.MOVE_BACKWARD.value, "stop_moving_forward")

    def test_when_start_moving_backward_given_is_already_moving_backward_then_should_keep_moving_backward_without_doing_anything_else(self):
        self.__test_start_movement_when_already_started("start_moving_backward", "is_moving_backward", "stop_moving_forward")

    def test_when_stop_moving_backward_given_is_moving_backward_then_should_stop_moving_backward(self):
        self.__test_stop_movement_when_started("stop_moving_backward", "is_moving_backward", KeySet.MOVE_BACKWARD.value)

    def test_when_stop_moving_backward_given_is_not_moving_backward_yet_then_should_stay_not_moving_backward(self):
         self.__test_stop_movement_when_not_started_yet("stop_moving_backward", "is_moving_backward")

    def test_when_start_moving_left_given_is_not_already_moving_left_then_should_start_moving_left_and_stop_moving_right(self):
        self.__test_start_movement_when_not_started_yet("start_moving_left", "is_moving_left", KeySet.MOVE_LEFT.value, "stop_moving_right")

    def test_when_start_moving_left_given_is_already_moving_left_then_should_keep_moving_left_without_doing_anything_else(self):
        self.__test_start_movement_when_already_started("start_moving_left", "is_moving_left", "stop_moving_right")

    def test_when_stop_moving_left_given_is_moving_left_then_should_stop_moving_left(self):
        self.__test_stop_movement_when_started("stop_moving_left", "is_moving_left", KeySet.MOVE_LEFT.value)

    def test_when_stop_moving_left_given_is_not_moving_left_yet_then_should_stay_not_moving_left(self):
         self.__test_stop_movement_when_not_started_yet("stop_moving_left", "is_moving_left")

    def test_when_start_moving_right_given_is_not_already_moving_right_then_should_start_moving_right_and_stop_moving_left(self):
        self.__test_start_movement_when_not_started_yet("start_moving_right", "is_moving_right", KeySet.MOVE_RIGHT.value, "stop_moving_left")

    def test_when_start_moving_right_given_is_already_moving_right_then_should_keep_moving_right_without_doing_anything_else(self):
        self.__test_start_movement_when_already_started("start_moving_right", "is_moving_right", "stop_moving_left")

    def test_when_stop_moving_right_given_is_moving_right_then_should_stop_moving_right(self):
        self.__test_stop_movement_when_started("stop_moving_right", "is_moving_right", KeySet.MOVE_RIGHT.value)

    def test_when_stop_moving_right_given_is_not_moving_right_yet_then_should_stay_not_moving_right(self):
         self.__test_stop_movement_when_not_started_yet("stop_moving_right", "is_moving_right")

    def __test_start_movement_when_not_started_yet(self, start_movement_method_name, movement_attribute_name, expected_key_set, countermovement_method_name):
        countermovement_method = getattr(self.movement_tracker, countermovement_method_name)
        self.original_countermovement_method = countermovement_method
        setattr(self.movement_tracker, countermovement_method_name, MagicMock("test_movement_tracker__" + countermovement_method_name))
        start_movement_method = getattr(self.movement_tracker, start_movement_method_name)
        start_movement_method()
        getattr(self.movement_tracker, countermovement_method_name).assert_called()
        self.test_util.assert_called_with_args_x_times(KeyOperator.press_keys, [expected_key_set], 1)
        self.assertTrue(getattr(self.movement_tracker, movement_attribute_name))
        setattr(self.movement_tracker, countermovement_method_name, self.original_countermovement_method)

    def __test_start_movement_when_already_started(self, start_movement_method_name, movement_attribute_name, countermovement_method_name):
        setattr(self.movement_tracker, movement_attribute_name, True)
        countermovement_method = getattr(self.movement_tracker, countermovement_method_name)
        self.original_countermovement_method = countermovement_method
        setattr(self.movement_tracker, countermovement_method_name, MagicMock("test_movement_tracker__" + countermovement_method_name))
        start_movement_method = getattr(self.movement_tracker, start_movement_method_name)
        start_movement_method()
        getattr(self.movement_tracker, countermovement_method_name).assert_not_called()
        KeyOperator.press_keys.assert_not_called()
        self.assertTrue(getattr(self.movement_tracker, movement_attribute_name))

    def __test_stop_movement_when_started(self, stop_movement_method_name, movement_attribute_name, expected_key_set):
        setattr(self.movement_tracker, movement_attribute_name, True)
        stop_movement_method = getattr(self.movement_tracker, stop_movement_method_name)
        stop_movement_method()
        self.test_util.assert_called_with_args_x_times(KeyOperator.release_keys, [expected_key_set], 1)
        self.assertFalse(getattr(self.movement_tracker, movement_attribute_name))

    def __test_stop_movement_when_not_started_yet(self, stop_movement_method_name, movement_attribute_name):
        stop_movement_method = getattr(self.movement_tracker, stop_movement_method_name)
        stop_movement_method()
        KeyOperator.release_keys.assert_not_called()
        self.assertFalse(getattr(self.movement_tracker, movement_attribute_name))
