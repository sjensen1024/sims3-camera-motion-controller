from src.input.key_operator import KeyOperator
from src.input.key_set import KeySet
from src.camera.movement_tracker import MovementTracker

class CameraOperator:
    def __init__(self):
        self.key_operator = KeyOperator()
        self.is_powered_on = False
        self.is_recording = False
        self.is_gameplay_paused = True
        self.movement_tracker = MovementTracker()

    def power_on(self):
        if self.is_powered_on: return
        self.__hit_key(KeySet.POWER.value)
        self.is_powered_on = True

    def power_off(self):
        if not self.is_powered_on: return
        self.__hit_key(KeySet.POWER.value)
        self.is_powered_on = False

    def start_recording(self):
        if self.is_recording: return
        self.__hit_key(KeySet.RECORD.value)
        self.is_recording = True

    def stop_recording(self):
        if not self.is_recording: return
        self.__hit_key(KeySet.RECORD.value)
        self.is_recording = False

    def pause_gameplay(self):
        if self.is_gameplay_paused: return
        self.__hit_key(KeySet.PAUSE.value)
        self.is_gameplay_paused = True

    def unpause_gameplay(self):
        if not self.is_gameplay_paused: return
        self.__hit_key(KeySet.PAUSE.value)
        self.is_gameplay_paused = False

    def take_snapshot(self):
        self.__hit_key(KeySet.SNAPSHOT.value)

    def __hit_key(self, key):
        self.key_operator.press_keys_without_holding([key])
    