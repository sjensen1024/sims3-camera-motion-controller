import unittest
import time
from unittest.mock import MagicMock
from tests.support.test_util import TestUtil
from src.camera.camera_operator import CameraOperator
from src.motion_control.action import Action
from src.motion_control.sequence import Sequence

class TestMotionControlSequence(unittest.TestCase):
    def setUp(self):
        self.test_util = TestUtil()
        self.original_time_sleep = time.sleep
        time.sleep = MagicMock("motion_control_sequence__time_sleep")
        self.original_action_run = Action.run
        Action.run = MagicMock("motion_control_sequence__action_run")

    def tearDown(self):
        time.sleep = self.original_time_sleep
        Action.run = self.original_action_run

    def test_when_init_given_duration_arg_is_less_than_zero_then_duration_defaults_to_10(self):
        sequence = Sequence(-1)
        self.assertEqual(sequence.duration_in_seconds, 10)

    def test_when_init_given_duration_arg_is_zero_then_duration_defaults_to_10(self):
        sequence = Sequence(0)
        self.assertEqual(sequence.duration_in_seconds, 10)

    def test_when_init_given_duration_arg_is_greater_than_zero_then_duration_is_set_to_that_duration_arg(self):
        sequence = Sequence(1)
        self.assertEqual(sequence.duration_in_seconds, 1)

    def test_when_run_given_added_four_actions_then_those_methods_should_get_called_at_certain_points_in_sequence(self):
        camera_operator = CameraOperator()
        start_recording_action = Action(0, camera_operator, "start_recording")
        start_moving_forward_action = Action(0.5, camera_operator.movement_tracker, "start_moving_forward")
        stop_moving_forward_action = Action(2, camera_operator.movement_tracker, "stop_moving_forward")
        stop_recording_action = Action(2.5, camera_operator, "stop_recording")
        sequence = Sequence(3)
        sequence.add_action(start_recording_action)
        sequence.add_action(start_moving_forward_action)
        sequence.add_action(stop_moving_forward_action)
        sequence.add_action(stop_recording_action)
        sequence.run()
        self.assertEqual(time.sleep.call_count, 7)
        start_recording_action.run.assert_called()
        start_moving_forward_action.run.assert_called()
        stop_moving_forward_action.run.assert_called()
        stop_recording_action.run.assert_called()
