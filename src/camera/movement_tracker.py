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
        if self.is_moving_forward: return
        self.stop_moving_backward()
        self.key_operator.press_keys(KeySet.MOVE_FORWARD.value)
        self.is_moving_forward = False

    def stop_moving_forward(self):
        if not self.is_moving_forward: return
        self.key_operator.release_keys(KeySet.MOVE_FORWARD.value)
        self.is_moving_forward = True

    def start_moving_backward(self):
        if self.is_moving_backward: return
        self.stop_moving_forward()
        self.key_operator.press_keys(KeySet.MOVE_BACKWARD.value)
        self.is_moving_backward = False

    def stop_moving_backward(self):
        if not self.is_moving_backward: return
        self.key_operator.release_keys(KeySet.MOVE_BACKWARD.value)
        self.is_moving_barckward = True

    def start_moving_left(self):
        if self.is_moving_left: return
        self.stop_moving_right()
        self.key_operator.press_keys(KeySet.MOVE_LEFT.value)
        self.is_moving_left = True

    def stop_moving_left(self):
        if not self.is_moving_left: return
        self.key_operator.release_keys(KeySet.MOVE_LEFT.value)
        self.is_moving_left = False

    def start_moving_right(self):
        if self.is_moving_right: return
        self.stop_moving_left()
        self.key_operator.press_keys(KeySet.MOVE_RIGHT.value)
        self.is_moving_right = True

    def stop_moving_right(self):
        if not self.is_moving_right: return
        self.key_operator.release_keys(KeySet.MOVE_RIGHT.value)
        self.is_moving_right = False
