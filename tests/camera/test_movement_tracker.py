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

    def test_suite_for_init(self):
        self.assertIsNotNone(self.movement_tracker.key_operator)
        self.__test_that_all_movement_tracking_boolean_attributes_are_false()

    def test_suite_for_moving_forward(self):
        test_args = ["start_moving_forward", "stop_moving_forward", "is_moving_forward", KeySet.MOVE_FORWARD.value, "stop_moving_backward"]
        self.__test_start_and_stop_method_scenarios_for_standard_movement(*test_args)

    def test_suite_for_moving_backward(self):
        test_args = ["start_moving_backward", "stop_moving_backward", "is_moving_backward", KeySet.MOVE_BACKWARD.value, "stop_moving_forward"]
        self.__test_start_and_stop_method_scenarios_for_standard_movement(*test_args)

    def test_suite_for_moving_left(self):
        test_args = ["start_moving_left", "stop_moving_left", "is_moving_left", KeySet.MOVE_LEFT.value, "stop_moving_right"]
        self.__test_start_and_stop_method_scenarios_for_standard_movement(*test_args)

    def test_suite_for_moving_right(self):
        test_args = ["start_moving_right", "stop_moving_right", "is_moving_right", KeySet.MOVE_RIGHT.value, "stop_moving_left"]
        self.__test_start_and_stop_method_scenarios_for_standard_movement(*test_args)

    def test_suite_for_raising(self):
        test_args = ["start_raising", "stop_raising", "is_raising", KeySet.RAISE.value, "stop_lowering"]
        self.__test_start_and_stop_method_scenarios_for_standard_movement(*test_args)

    def test_suite_for_lowering(self):
        test_args = ["start_lowering", "stop_lowering", "is_lowering", KeySet.LOWER.value, "stop_raising"]
        self.__test_start_and_stop_method_scenarios_for_standard_movement(*test_args)

    def test_suite_for_zooming_in(self):
        test_args = ["start_zooming_in", "stop_zooming_in", "is_zooming_in", KeySet.ZOOM_IN.value, "stop_zooming_out"]
        self.__test_start_and_stop_method_scenarios_for_standard_movement(*test_args)

    def test_suite_for_zooming_out(self):
        test_args = ["start_zooming_out", "stop_zooming_out", "is_zooming_out", KeySet.ZOOM_OUT.value, "stop_zooming_in"]
        self.__test_start_and_stop_method_scenarios_for_standard_movement(*test_args)

    def test_suite_for_rotating_left(self):
        test_args = ["start_rotating_left", "stop_rotating_left", "is_rotating_left", KeySet.ROTATE_LEFT.value, "stop_rotating_right"]
        self.__test_start_and_stop_method_scenarios_for_standard_movement(*test_args)

    def test_suite_for_rotating_right(self):
        test_args = ["start_rotating_right", "stop_rotating_right", "is_rotating_right", KeySet.ROTATE_RIGHT.value, "stop_rotating_left"]
        self.__test_start_and_stop_method_scenarios_for_standard_movement(*test_args)

    def test_suite_for_turning_left(self):
        test_args = ["start_turning_left", "stop_turning_left", "is_turning_left", KeySet.TURN_LEFT.value, "stop_turning_right"]
        self.__test_start_and_stop_method_scenarios_for_standard_movement(*test_args)

    def test_suite_for_turning_right(self):
        test_args = ["start_turning_right", "stop_turning_right", "is_turning_right", KeySet.TURN_RIGHT.value, "stop_turning_left"]
        self.__test_start_and_stop_method_scenarios_for_standard_movement(*test_args)

    def test_when_stop_all_tracked_movements_given_flags_were_set_to_true_then_now_they_should_all_be_false(self):
        self.__setup_release_keys_mock()
        self.movement_tracker.is_moving_forward = True
        self.movement_tracker.is_moving_backward = True
        self.movement_tracker.is_moving_left = True
        self.movement_tracker.is_moving_right = True
        self.movement_tracker.is_raising = True
        self.movement_tracker.is_lowering = True
        self.movement_tracker.is_zooming_in = True
        self.movement_tracker.is_zooming_out = True
        self.movement_tracker.is_rotating_left = True
        self.movement_tracker.is_rotating_right = True
        self.movement_tracker.is_turning_left = True
        self.movement_tracker.is_turning_right = True
        self.movement_tracker.stop_all_tracked_movements()
        self.__test_that_all_movement_tracking_boolean_attributes_are_false()
        self.__teardown_release_keys_mock()

    def test_when_level_out_then_should_hit_correct_key_and_stop_all_tracked_movements(self):
         self.__test_method_that_hits_keys_and_stops_all_other_movements('level_out', KeySet.LEVEL_OUT.value)

    def test_when_move_to_position_5_then_should_hit_correct_key_and_stop_all_tracked_movements(self):
         self.__test_method_that_hits_keys_and_stops_all_other_movements('move_to_position_5', KeySet.MOVE_TO_POSITION_5.value)

    def test_when_move_to_position_6_then_should_hit_correct_key_and_stop_all_tracked_movements(self):
         self.__test_method_that_hits_keys_and_stops_all_other_movements('move_to_position_6', KeySet.MOVE_TO_POSITION_6.value)

    def test_when_move_to_position_7_then_should_hit_correct_key_and_stop_all_tracked_movements(self):
         self.__test_method_that_hits_keys_and_stops_all_other_movements('move_to_position_7', KeySet.MOVE_TO_POSITION_7.value)

    def test_when_move_to_position_8_then_should_hit_correct_key_and_stop_all_tracked_movements(self):
         self.__test_method_that_hits_keys_and_stops_all_other_movements('move_to_position_8', KeySet.MOVE_TO_POSITION_8.value)

    def test_when_move_to_position_9_then_should_hit_correct_key_and_stop_all_tracked_movements(self):
         self.__test_method_that_hits_keys_and_stops_all_other_movements('move_to_position_9', KeySet.MOVE_TO_POSITION_9.value)

    def test_when_snap_to_position_5_then_should_hit_correct_key_and_stop_all_tracked_movements(self):
         self.__test_method_that_hits_keys_and_stops_all_other_movements('snap_to_position_5', KeySet.SNAP_TO_POSITION_5.value)

    def test_when_snap_to_position_6_then_should_hit_correct_key_and_stop_all_tracked_movements(self):
         self.__test_method_that_hits_keys_and_stops_all_other_movements('snap_to_position_6', KeySet.SNAP_TO_POSITION_6.value)

    def test_when_snap_to_position_7_then_should_hit_correct_key_and_stop_all_tracked_movements(self):
         self.__test_method_that_hits_keys_and_stops_all_other_movements('snap_to_position_7', KeySet.SNAP_TO_POSITION_7.value)

    def test_when_snap_to_position_8_then_should_hit_correct_key_and_stop_all_tracked_movements(self):
         self.__test_method_that_hits_keys_and_stops_all_other_movements('snap_to_position_8', KeySet.SNAP_TO_POSITION_8.value)

    def test_when_snap_to_position_9_then_should_hit_correct_key_and_stop_all_tracked_movements(self):
         self.__test_method_that_hits_keys_and_stops_all_other_movements('snap_to_position_9', KeySet.SNAP_TO_POSITION_9.value)

    def __test_start_and_stop_method_scenarios_for_standard_movement(self, 
                                                                     start_movement_method_name, 
                                                                     stop_movement_method_name, 
                                                                     movement_attribute_name,
                                                                     movement_key_set, 
                                                                     stop_countermovement_method_name):
        self.__test_start_movement_when_not_started_yet(start_movement_method_name, movement_attribute_name, movement_key_set, stop_countermovement_method_name)
        self.__test_start_movement_when_already_started(start_movement_method_name, movement_attribute_name, stop_countermovement_method_name)
        self.__test_stop_movement_when_started(stop_movement_method_name, movement_attribute_name, movement_key_set)
        self.__test_stop_movement_when_not_started_yet(stop_movement_method_name, movement_attribute_name)
        

    def __test_start_movement_when_not_started_yet(self, 
                                                   start_movement_method_name, 
                                                   movement_attribute_name, 
                                                   expected_key_set, 
                                                   countermovement_method_name):
        self.__setup_press_keys_mock()
        countermovement_method = getattr(self.movement_tracker, countermovement_method_name)
        self.original_countermovement_method = countermovement_method
        setattr(self.movement_tracker, countermovement_method_name, MagicMock("test_movement_tracker__" + countermovement_method_name))
        start_movement_method = getattr(self.movement_tracker, start_movement_method_name)
        start_movement_method()
        getattr(self.movement_tracker, countermovement_method_name).assert_called()
        self.test_util.assert_called_with_args_x_times(KeyOperator.press_keys, [expected_key_set], 1)
        self.assertTrue(getattr(self.movement_tracker, movement_attribute_name))
        setattr(self.movement_tracker, countermovement_method_name, self.original_countermovement_method)
        self.__teardown_press_keys_mock()

    def __test_start_movement_when_already_started(self, 
                                                   start_movement_method_name, 
                                                   movement_attribute_name, 
                                                   countermovement_method_name):
        self.__setup_press_keys_mock()
        setattr(self.movement_tracker, movement_attribute_name, True)
        countermovement_method = getattr(self.movement_tracker, countermovement_method_name)
        self.original_countermovement_method = countermovement_method
        setattr(self.movement_tracker, countermovement_method_name, MagicMock("test_movement_tracker__" + countermovement_method_name))
        start_movement_method = getattr(self.movement_tracker, start_movement_method_name)
        start_movement_method()
        getattr(self.movement_tracker, countermovement_method_name).assert_not_called()
        KeyOperator.press_keys.assert_not_called()
        self.assertTrue(getattr(self.movement_tracker, movement_attribute_name))
        self.__teardown_press_keys_mock()

    def __test_stop_movement_when_started(self, stop_movement_method_name, movement_attribute_name, expected_key_set):
        self.__setup_release_keys_mock()
        setattr(self.movement_tracker, movement_attribute_name, True)
        stop_movement_method = getattr(self.movement_tracker, stop_movement_method_name)
        stop_movement_method()
        self.test_util.assert_called_with_args_x_times(KeyOperator.release_keys, [expected_key_set], 1)
        self.assertFalse(getattr(self.movement_tracker, movement_attribute_name))
        self.__teardown_release_keys_mock()

    def __test_stop_movement_when_not_started_yet(self, stop_movement_method_name, movement_attribute_name):
        self.__setup_release_keys_mock()
        stop_movement_method = getattr(self.movement_tracker, stop_movement_method_name)
        stop_movement_method()
        KeyOperator.release_keys.assert_not_called()
        self.assertFalse(getattr(self.movement_tracker, movement_attribute_name))
        self.__teardown_release_keys_mock()

    def __test_that_all_movement_tracking_boolean_attributes_are_false(self):
        self.assertFalse(self.movement_tracker.is_moving_forward)
        self.assertFalse(self.movement_tracker.is_moving_backward)
        self.assertFalse(self.movement_tracker.is_moving_left)
        self.assertFalse(self.movement_tracker.is_moving_right)
        self.assertFalse(self.movement_tracker.is_raising)
        self.assertFalse(self.movement_tracker.is_lowering)
        self.assertFalse(self.movement_tracker.is_zooming_in)
        self.assertFalse(self.movement_tracker.is_zooming_out)
        self.assertFalse(self.movement_tracker.is_rotating_left)
        self.assertFalse(self.movement_tracker.is_rotating_right)
        self.assertFalse(self.movement_tracker.is_turning_left)
        self.assertFalse(self.movement_tracker.is_turning_right)

    def __test_method_that_hits_keys_and_stops_all_other_movements(self, method_name, keys):
        self.original_hit_keys = KeyOperator.press_keys_without_holding
        KeyOperator.press_keys_without_holding = MagicMock("test_movement_tracker__press_keys_without_holding")
        self.original_stop_all_tracked_movements = MovementTracker.stop_all_tracked_movements
        MovementTracker.stop_all_tracked_movements = MagicMock("test_movement_tracker__stop_all_tracked_movements")
        method_to_test = getattr(self.movement_tracker, method_name)
        method_to_test()
        self.test_util.assert_called_with_args_x_times(KeyOperator.press_keys_without_holding, [keys], 1)
        MovementTracker.stop_all_tracked_movements.assert_called()
        KeyOperator.press_keys_without_holding = self.original_hit_keys
        MovementTracker.stop_all_tracked_movements = self.original_stop_all_tracked_movements

    def __setup_press_keys_mock(self):
        self.original_press_keys = KeyOperator.press_keys
        KeyOperator.press_keys = MagicMock("test_movement_tracker__press_keys")
        
    def __setup_release_keys_mock(self):
        self.original_release_keys = KeyOperator.release_keys
        KeyOperator.release_keys = MagicMock("test_movement_tracker__release_keys")

    def __teardown_press_keys_mock(self):
        KeyOperator.press_keys = self.original_press_keys

    def __teardown_release_keys_mock(self):
        KeyOperator.release_keys = self.original_release_keys
