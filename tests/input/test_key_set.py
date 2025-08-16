import unittest
from pynput.keyboard import Key
from src.input.key_set import KeySet

class TestKeySet(unittest.TestCase):
    def test_when_getting_camera_control_value_given_name_is_power_then_value_list_is_tab_key(self):
        self.assertEqual(KeySet.POWER.value, [Key.tab])

    def test_when_getting_camera_control_value_given_name_is_record_then_value_list_is_v(self):
        self.assertEqual(KeySet.RECORD.value, ['v']) 

    def test_when_getting_camera_control_value_given_name_is_pause_then_value_list_is_p(self):
        self.assertEqual(KeySet.PAUSE.value, ['p'])

    def test_when_getting_camera_control_value_given_name_is_snapshot_then_value_list_is_c(self):
        self.assertEqual(KeySet.SNAPSHOT.value, ['c'])

    def test_when_getting_camera_control_value_given_name_is_lower_then_value_list_is_q(self):
        self.assertEqual(KeySet.LOWER.value, ['q'])

    def test_when_getting_camera_control_value_given_name_is_raise_then_value_list_is_e(self):
        self.assertEqual(KeySet.RAISE.value, ['e'])

    def test_when_getting_camera_control_value_given_name_is_move_forward_then_value_list_is_w(self):
        self.assertEqual(KeySet.MOVE_FORWARD.value, ['w'])

    def test_when_getting_camera_control_value_given_name_is_move_backward_then_value_list_is_s(self):
        self.assertEqual(KeySet.MOVE_BACKWARD.value, ['s'])

    def test_when_getting_camera_control_value_given_name_is_move_left_then_value_list_is_a(self):
        self.assertEqual(KeySet.MOVE_LEFT.value, ['a'])
    
    def test_when_getting_camera_control_value_given_name_is_move_right_then_value_list_is_d(self):
        self.assertEqual(KeySet.MOVE_RIGHT.value, ['d'])

    def test_when_getting_camera_control_value_given_name_is_zoom_in_then_value_list_is_z(self):
        self.assertEqual(KeySet.ZOOM_IN.value, ['z'])

    def test_when_getting_camera_control_value_given_name_is_zoom_out_then_value_list_is_x(self):
        self.assertEqual(KeySet.ZOOM_OUT.value, ['x'])

    def test_when_getting_camera_control_value_given_name_is_level_out_then_value_list_is_shift_and_s(self):
        self.assertEqual(KeySet.LEVEL_OUT.value, [Key.shift, 's'])

    def test_when_getting_camera_control_value_given_name_is_rotate_left_then_value_list_is_shift_and_a(self):
        self.assertEqual(KeySet.ROTATE_LEFT.value, [Key.shift, 'a'])

    def test_when_getting_camera_control_value_given_name_is_rotate_right_then_value_list_is_shift_and_d(self):
        self.assertEqual(KeySet.ROTATE_RIGHT.value, [Key.shift, 'd'])

    def test_when_getting_camera_control_value_given_name_is_turn_left_then_value_list_is_comma(self):
        self.assertEqual(KeySet.TURN_LEFT.value, [','])

    def test_when_getting_camera_control_value_given_name_is_turn_right_then_value_list_is_period(self):
        self.assertEqual(KeySet.TURN_RIGHT.value, ['.'])

    def test_when_getting_camera_control_value_given_name_is_move_to_position_5_then_value_list_is_5(self):
        self.assertEqual(KeySet.MOVE_TO_POSITION_5.value, ['5'])

    def test_when_getting_camera_control_value_given_name_is_move_to_position_6_then_value_list_is_6(self):
        self.assertEqual(KeySet.MOVE_TO_POSITION_6.value, ['6'])

    def test_when_getting_camera_control_value_given_name_is_move_to_position_7_then_value_list_is_7(self):
        self.assertEqual(KeySet.MOVE_TO_POSITION_7.value, ['7'])

    def test_when_getting_camera_control_value_given_name_is_move_to_position_8_then_value_list_is_8(self):
        self.assertEqual(KeySet.MOVE_TO_POSITION_8.value, ['8'])

    def test_when_getting_camera_control_value_given_name_is_move_to_position_9_then_value_list_is_9(self):
        self.assertEqual(KeySet.MOVE_TO_POSITION_9.value, ['9'])

    def test_when_getting_camera_control_value_given_name_is_snap_to_position_5_then_value_list_is_shift_and_5(self):
        self.assertEqual(KeySet.SNAP_TO_POSITION_5.value, [Key.shift, '5'])

    def test_when_getting_camera_control_value_given_name_is_snap_to_position_6_then_value_list_is_shift_and_6(self):
        self.assertEqual(KeySet.SNAP_TO_POSITION_6.value, [Key.shift, '6'])

    def test_when_getting_camera_control_value_given_name_is_snap_to_position_7_then_value_list_is_shift_and_7(self):
        self.assertEqual(KeySet.SNAP_TO_POSITION_7.value, [Key.shift, '7'])

    def test_when_getting_camera_control_value_given_name_is_snap_to_position_8_then_value_list_is_shift_and_8(self):
        self.assertEqual(KeySet.SNAP_TO_POSITION_8.value, [Key.shift, '8'])

    def test_when_getting_camera_control_value_given_name_is_snap_to_position_9_then_value_list_is_shift_and_9(self):
        self.assertEqual(KeySet.SNAP_TO_POSITION_9.value, [Key.shift, '9'])
