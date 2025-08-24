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

    def test_when_run_given_various_actions_then_should_only_run_actions_at_valid_increments_within_duration_even_if_they_are_the_same(self):
        camera_operator = CameraOperator()
        in_bounds_action_1 = Action(0, camera_operator.start_recording)
        in_bounds_action_2_with_duplicate_increment = Action(0.5, camera_operator.movement_tracker.start_moving_forward)
        in_bounds_action_3_with_duplicate_increment = Action(0.5, camera_operator.movement_tracker.start_raising)
        in_bounds_action_4_with_duplicate_increment = Action(2, camera_operator.movement_tracker.stop_moving_forward)
        in_bounds_action_5_with_duplicate_increment = Action(2, camera_operator.movement_tracker.stop_raising)
        in_bounds_action_6_with_duplicate_increment = Action(2.5, camera_operator.stop_recording)
        out_of_bounds_action = Action(5, camera_operator.take_snapshot)
        in_bounds_but_not_at_valid_increment_action = Action(2.75, camera_operator.pause_gameplay)
        sequence = Sequence(3)
        sequence.add_action(in_bounds_action_1)
        sequence.add_action(in_bounds_action_2_with_duplicate_increment)
        sequence.add_action(in_bounds_action_3_with_duplicate_increment)
        sequence.add_action(in_bounds_action_4_with_duplicate_increment)
        sequence.add_action(in_bounds_action_5_with_duplicate_increment)
        sequence.add_action(in_bounds_action_6_with_duplicate_increment)
        sequence.add_action(out_of_bounds_action)
        sequence.add_action(in_bounds_but_not_at_valid_increment_action)
        sequence.run()
        self.assertEqual(time.sleep.call_count, 7)
        self.assertEqual(Action.run.call_count, 6)
