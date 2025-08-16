import unittest
from unittest.mock import MagicMock
from src.input.key_operator import KeyOperator
from src.input.key_set import KeySet
from tests.support.test_util import TestUtil
from src.camera.camera_operator import CameraOperator

class TestCameraOperator(unittest.TestCase):
    def setUp(self):
        self.camera_operator = CameraOperator()
        self.test_util = TestUtil()
        self.original_press_keys_without_holding = KeyOperator.press_keys_without_holding
        KeyOperator.press_keys_without_holding = MagicMock("test_camera_operator__press_keys_without_holding")

    def tearDown(self):
        KeyOperator.press_keys_without_holding = self.original_press_keys_without_holding

    def test_when_init_given_checking_key_operator_then_should_start_out_with_a_not_none_key_operator(self):
        self.assertIsNotNone(self.camera_operator.key_operator)

    def test_when_init_given_checking_is_powered_on_then_should_start_out_assuming_camera_powered_off(self):
        self.assertFalse(self.camera_operator.is_powered_on)

    def test_when_init_given_checking_is_recording_then_should_start_out_assuming_camera_is_not_recording(self):    
        self.assertFalse(self.camera_operator.is_recording)
    
    def test_when_init_given_checking_is_gameplay_paused_then_should_start_out_assuming_gameplay_is_paused(self):
        self.assertTrue(self.camera_operator.is_gameplay_paused)  

    def test_when_init_given_checking_movement_tracker_then_should_start_out_a_not_none_movement_tracker(self):
        self.assertIsNotNone(self.camera_operator.movement_tracker)

    def test_when_power_on_given_camera_is_not_already_powered_on_then_should_press_power_key_and_toggle_power_on(self):
        self.camera_operator.power_on()
        self.test_util.assert_called_with_args_x_times(KeyOperator.press_keys_without_holding, [[KeySet.POWER.value]], 1)
        self.assertTrue(self.camera_operator.is_powered_on)

    def test_when_power_on_given_camera_is_already_powered_on_then_should_not_press_power_key_and_should_still_be_powered_on(self):
        self.camera_operator.is_powered_on = True
        self.camera_operator.power_on()
        KeyOperator.press_keys_without_holding.assert_not_called()
        self.assertTrue(self.camera_operator.is_powered_on)

    def test_when_power_off_given_camera_is_not_already_powered_off_then_should_press_power_key_and_toggle_power_off(self):
        self.camera_operator.is_powered_on = True
        self.camera_operator.power_off()
        self.test_util.assert_called_with_args_x_times(KeyOperator.press_keys_without_holding, [[KeySet.POWER.value]], 1)
        self.assertFalse(self.camera_operator.is_powered_on)

    def test_when_power_on_given_camera_is_already_powered_on_then_should_not_press_power_key_and_should_still_be_powered_on(self):
        self.camera_operator.power_off()
        KeyOperator.press_keys_without_holding.assert_not_called()
        self.assertFalse(self.camera_operator.is_powered_on)

    def test_when_start_recording_given_camera_is_not_already_recording_then_should_press_record_key_and_be_recording(self):
        self.camera_operator.start_recording()
        self.test_util.assert_called_with_args_x_times(KeyOperator.press_keys_without_holding, [[KeySet.RECORD.value]], 1)
        self.assertTrue(self.camera_operator.is_recording)
        
    def test_when_start_recording_given_camera_is_already_recording_then_should_not_press_record_key_and_should_still_be_recording(self):
        self.camera_operator.is_recording = True
        self.camera_operator.start_recording()
        KeyOperator.press_keys_without_holding.assert_not_called()
        self.assertTrue(self.camera_operator.is_recording)

    def test_when_stop_recording_given_camera_is_recording_then_should_press_record_key_and_stop_recording(self):
        self.camera_operator.is_recording = True
        self.camera_operator.stop_recording()
        self.test_util.assert_called_with_args_x_times(KeyOperator.press_keys_without_holding, [[KeySet.RECORD.value]], 1)
        self.assertFalse(self.camera_operator.is_recording)
        
    def test_when_start_recording_given_camera_is_already_not_recording_then_should_not_press_record_key_and_should_still_not_be_recording(self):
        self.camera_operator.stop_recording()
        KeyOperator.press_keys_without_holding.assert_not_called()
        self.assertFalse(self.camera_operator.is_recording)

    def test_when_pause_gameplay_given_gameplay_is_not_paused_then_should_press_pause_key_and_gameplay_should_be_paused(self):
        self.camera_operator.is_gameplay_paused = False
        self.camera_operator.pause_gameplay()
        self.test_util.assert_called_with_args_x_times(KeyOperator.press_keys_without_holding, [[KeySet.PAUSE.value]], 1)
        self.assertTrue(self.camera_operator.is_gameplay_paused)

    def test_when_pause_gameplay_given_gameplay_is_already_paused_then_should_not_press_pause_key_and_gameplay_should_still_be_paused(self):
        self.camera_operator.pause_gameplay()
        KeyOperator.press_keys_without_holding.assert_not_called()
        self.assertTrue(self.camera_operator.is_gameplay_paused)

    def test_when_unpause_gameplay_given_gameplay_is_paused_then_should_press_pause_key_and_gameplay_should_be_unpaused(self):
        self.camera_operator.unpause_gameplay()
        self.test_util.assert_called_with_args_x_times(KeyOperator.press_keys_without_holding, [[KeySet.PAUSE.value]], 1)
        self.assertFalse(self.camera_operator.is_gameplay_paused)

    def test_when_unpause_gameplay_given_gameplay_is_already_unpaused_then_should_not_press_pause_key_and_gameplay_should_still_be_unpaused(self):
        self.camera_operator.is_gameplay_paused = False
        self.camera_operator.unpause_gameplay()
        KeyOperator.press_keys_without_holding.assert_not_called()
        self.assertFalse(self.camera_operator.is_gameplay_paused)

    def test_when_take_snapshot_then_should_press_snapshot_key(self):
        self.camera_operator.take_snapshot()
        # TODO: Check what happens in-game if you are already recording video and try to take a snapshot.
        self.test_util.assert_called_with_args_x_times(KeyOperator.press_keys_without_holding, [[KeySet.SNAPSHOT.value]], 1)
    