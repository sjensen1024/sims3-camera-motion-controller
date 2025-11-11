import unittest
from unittest.mock import MagicMock
from src.camera.camera_operator import CameraOperator
from src.camera.movement_tracker import MovementTracker
from src.motion_control.action import Action

class TestMotionControlAction(unittest.TestCase):
    def setUp(self):
        self.original_camera_operator_power_on = CameraOperator.power_on
        CameraOperator.power_on = MagicMock("test_action__camera_operator_power_on")
        self.original_movement_tracker_start_moving_forward = MovementTracker.start_moving_forward
        MovementTracker.start_moving_forward = MagicMock("test_action__movement_tracker_start_moving_forward")
        self.test_camera_operator = CameraOperator()
        self.test_camera_operator_action = Action(0.5, self.test_camera_operator.power_on)
        self.test_movement_tracker = MovementTracker()
        self.test_movement_tracker_action = Action(1.5, self.test_movement_tracker.start_moving_forward)

    def tearDown(self):
        CameraOperator.power_on = self.original_camera_operator_power_on
        MovementTracker.start_moving_forward = self.original_movement_tracker_start_moving_forward

    def test_suite_for_camera_operator_action(self):
       self._assert_action_is_initialized_correctly(
           self.test_camera_operator_action, 
           0.5, 
           self.test_camera_operator.power_on
        )
       self._assert_run_calls_method_from_caller(self.test_camera_operator_action)

    def test_suite_for_movement_tracker_action(self):
        self._assert_action_is_initialized_correctly(
            self.test_movement_tracker_action, 
            1.5, 
            self.test_movement_tracker.start_moving_forward
        )
        self._assert_run_calls_method_from_caller(self.test_movement_tracker_action)


    def _assert_action_is_initialized_correctly(self, action, expected_seconds_in, expected_method_to_call):
        self.assertEqual(action.run_at_this_many_seconds_in, expected_seconds_in)
        self.assertEqual(action.method_to_call, expected_method_to_call)

    def _assert_run_calls_method_from_caller(self, action):
        action.run()
        action.method_to_call.assert_called()
        