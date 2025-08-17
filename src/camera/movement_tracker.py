from src.input.key_operator import KeyOperator
from src.input.key_set import KeySet

class MovementTracker:
    def __init__(self):
        self.key_operator = KeyOperator
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
        self.__process_standard_start_movement('is_moving_forward', KeySet.MOVE_FORWARD.value, ['stop_moving_backward'])

    def stop_moving_forward(self):
        self.__process_standard_stop_movement('is_moving_forward', KeySet.MOVE_FORWARD.value)

    def start_moving_backward(self):
        self.__process_standard_start_movement('is_moving_backward', KeySet.MOVE_BACKWARD.value, ['stop_moving_forward'])

    def stop_moving_backward(self):
        self.__process_standard_stop_movement('is_moving_backward', KeySet.MOVE_BACKWARD.value)

    def start_moving_left(self):
        self.__process_standard_start_movement('is_moving_left', KeySet.MOVE_LEFT.value, ['stop_moving_right'])

    def stop_moving_left(self):
        self.__process_standard_stop_movement('is_moving_left', KeySet.MOVE_LEFT.value)

    def start_moving_right(self):
        self.__process_standard_start_movement('is_moving_right', KeySet.MOVE_RIGHT.value, ['stop_moving_left'])

    def stop_moving_right(self):
        self.__process_standard_stop_movement('is_moving_right', KeySet.MOVE_RIGHT.value)

    def __process_standard_start_movement(self, attribute_name, key_set_to_press, impossible_movements_to_stop = []):
        if getattr(self, attribute_name): return
        for impossible_movement_to_stop in impossible_movements_to_stop:
            method = getattr(self, impossible_movement_to_stop)
            method()
        self.key_operator.press_keys(key_set_to_press)
        setattr(self, attribute_name, True)

    def __process_standard_stop_movement(self, attribute_name, key_set_to_release):
        if not getattr(self, attribute_name): return
        self.key_operator.release_keys(key_set_to_release)
        setattr(self, attribute_name, False)
