from src.input.key_operator import KeyOperator
from src.input.key_set import KeySet

class MovementTracker:
    def __init__(self):
        self.key_operator = KeyOperator()
        self.is_moving_forward = False
        self.is_moving_backward = False
        self.is_moving_left = False
        self.is_moving_right = False
        self.is_raising = False
        self.is_lowering = False
        self.is_zooming_in = False
        self.is_zooming_out = False
        self.is_rotating_left = False
        self.is_rotating_right = False
        self.is_turning_left = False
        self.is_turning_right = False

    def start_moving_forward(self):
        self._process_standard_start_movement('is_moving_forward', KeySet.MOVE_FORWARD.value, ['stop_moving_backward'])

    def stop_moving_forward(self):
        self._process_standard_stop_movement('is_moving_forward', KeySet.MOVE_FORWARD.value)

    def start_moving_backward(self):
        self._process_standard_start_movement('is_moving_backward', KeySet.MOVE_BACKWARD.value, ['stop_moving_forward'])

    def stop_moving_backward(self):
        self._process_standard_stop_movement('is_moving_backward', KeySet.MOVE_BACKWARD.value)

    def start_moving_left(self):
        self._process_standard_start_movement('is_moving_left', KeySet.MOVE_LEFT.value, ['stop_moving_right'])

    def stop_moving_left(self):
        self._process_standard_stop_movement('is_moving_left', KeySet.MOVE_LEFT.value)

    def start_moving_right(self):
        self._process_standard_start_movement('is_moving_right', KeySet.MOVE_RIGHT.value, ['stop_moving_left'])

    def stop_moving_right(self):
        self._process_standard_stop_movement('is_moving_right', KeySet.MOVE_RIGHT.value)

    def start_raising(self):
        self._process_standard_start_movement('is_raising', KeySet.RAISE.value, ['stop_lowering'])

    def stop_raising(self):
        self._process_standard_stop_movement('is_raising', KeySet.RAISE.value)

    def start_lowering(self):
        self._process_standard_start_movement('is_lowering', KeySet.LOWER.value, ['stop_raising'])

    def stop_lowering(self):
        self._process_standard_stop_movement('is_lowering', KeySet.LOWER.value)

    def start_zooming_in(self):
        self._process_standard_start_movement('is_zooming_in', KeySet.ZOOM_IN.value, ['stop_zooming_out'])
    
    def stop_zooming_in(self):
        self._process_standard_stop_movement('is_zooming_in', KeySet.ZOOM_IN.value)

    def start_zooming_out(self):
        self._process_standard_start_movement('is_zooming_out', KeySet.ZOOM_OUT.value, ['stop_zooming_in'])

    def stop_zooming_out(self):
        self._process_standard_stop_movement('is_zooming_out', KeySet.ZOOM_OUT.value)

    def start_rotating_left(self):
        self._process_standard_start_movement('is_rotating_left', KeySet.ROTATE_LEFT.value, ['stop_rotating_right'])

    def stop_rotating_left(self):
        self._process_standard_stop_movement('is_rotating_left', KeySet.ROTATE_LEFT.value)

    def start_rotating_right(self):
        self._process_standard_start_movement('is_rotating_right', KeySet.ROTATE_RIGHT.value, ['stop_rotating_left'])

    def stop_rotating_right(self):
        self._process_standard_stop_movement('is_rotating_right', KeySet.ROTATE_RIGHT.value)

    def start_turning_left(self):
        self._process_standard_start_movement('is_turning_left', KeySet.TURN_LEFT.value, ['stop_turning_right'])

    def stop_turning_left(self):
        self._process_standard_stop_movement('is_turning_left', KeySet.TURN_LEFT.value)

    def start_turning_right(self):
        self._process_standard_start_movement('is_turning_right', KeySet.TURN_RIGHT.value, ['stop_turning_left'])

    def stop_turning_right(self):
        self._process_standard_stop_movement('is_turning_right', KeySet.TURN_RIGHT.value)

    def level_out(self):
        self._process_movement_that_stops_all_others(KeySet.LEVEL_OUT.value)

    def move_to_position_5(self):
        self._process_movement_that_stops_all_others(KeySet.MOVE_TO_POSITION_5.value)

    def move_to_position_6(self):
        self._process_movement_that_stops_all_others(KeySet.MOVE_TO_POSITION_6.value)

    def move_to_position_7(self):
        self._process_movement_that_stops_all_others(KeySet.MOVE_TO_POSITION_7.value)

    def move_to_position_8(self):
        self._process_movement_that_stops_all_others(KeySet.MOVE_TO_POSITION_8.value)

    def move_to_position_9(self):
        self._process_movement_that_stops_all_others(KeySet.MOVE_TO_POSITION_9.value)

    def snap_to_position_5(self):
        self._process_movement_that_stops_all_others(KeySet.SNAP_TO_POSITION_5.value)

    def snap_to_position_6(self):
        self._process_movement_that_stops_all_others(KeySet.SNAP_TO_POSITION_6.value)

    def snap_to_position_7(self):
        self._process_movement_that_stops_all_others(KeySet.SNAP_TO_POSITION_7.value)

    def snap_to_position_8(self):
        self._process_movement_that_stops_all_others(KeySet.SNAP_TO_POSITION_8.value)

    def snap_to_position_9(self):
        self._process_movement_that_stops_all_others(KeySet.SNAP_TO_POSITION_9.value)

    def stop_all_tracked_movements(self):
        self.stop_moving_forward()
        self.stop_moving_backward()
        self.stop_moving_left()
        self.stop_moving_right()
        self.stop_raising()
        self.stop_lowering()
        self.stop_zooming_in()
        self.stop_zooming_out()
        self.stop_rotating_left()
        self.stop_rotating_right()
        self.stop_turning_left()
        self.stop_turning_right()

    def _process_standard_start_movement(self, attribute_name, key_set_to_press, impossible_movements_to_stop = []):
        if getattr(self, attribute_name): return
        for impossible_movement_to_stop in impossible_movements_to_stop:
            method = getattr(self, impossible_movement_to_stop)
            method()
        self.key_operator.press_keys(key_set_to_press)
        setattr(self, attribute_name, True)

    def _process_standard_stop_movement(self, attribute_name, key_set_to_release):
        if not getattr(self, attribute_name): return
        self.key_operator.release_keys(key_set_to_release)
        setattr(self, attribute_name, False)

    def _process_movement_that_stops_all_others(self, key_set_to_hit):
        self.key_operator.press_keys_without_holding(key_set_to_hit)
        self.stop_all_tracked_movements()
