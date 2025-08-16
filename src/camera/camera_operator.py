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
        self.__process_standard_toggle_on_key_hit('is_powered_on', KeySet.POWER.value)

    def power_off(self):
        self.__process_standard_toggle_off_key_hit('is_powered_on', KeySet.POWER.value)

    def start_recording(self):
        self.__process_standard_toggle_on_key_hit('is_recording', KeySet.RECORD.value)

    def stop_recording(self):
        self.__process_standard_toggle_off_key_hit('is_recording', KeySet.RECORD.value)

    def pause_gameplay(self):
        self.__process_standard_toggle_on_key_hit('is_gameplay_paused', KeySet.PAUSE.value)

    def unpause_gameplay(self):
        self.__process_standard_toggle_off_key_hit('is_gameplay_paused', KeySet.PAUSE.value)

    def take_snapshot(self):
        self.__hit_key(KeySet.SNAPSHOT.value)

    def __process_standard_toggle_on_key_hit(self, attribute_name, key_set_to_hit):
        if getattr(self, attribute_name): return
        self.__hit_key(key_set_to_hit)
        setattr(self, attribute_name, True)
        
    def __process_standard_toggle_off_key_hit(self, attribute_name, key_set_to_hit):
        if not getattr(self, attribute_name): return
        self.__hit_key(key_set_to_hit)
        setattr(self, attribute_name, False)

    def __hit_key(self, key):
        self.key_operator.press_keys_without_holding([key])
    