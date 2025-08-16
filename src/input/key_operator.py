import time
from pynput.keyboard import Controller

class KeyOperator:
    def __init__(self):
        self.keyboard_controller = Controller()

    def press_keys_without_holding(self, keys):
        self.press_keys(keys)
        self.release_keys(keys)

    def press_and_hold_keys(self, keys, hold_time_in_seconds):
        self.press_keys(keys)
        time.sleep(hold_time_in_seconds)
        self.release_keys(keys)
        
    def press_keys(self, keys):
        [self.keyboard_controller.press(key) for key in keys]

    def release_keys(self, keys):
        [self.keyboard_controller.release(key) for key in keys]
           