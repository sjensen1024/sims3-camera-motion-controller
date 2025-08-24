from src.camera.camera_operator import CameraOperator
from src.motion_control.action import Action
from src.motion_control.sequence import Sequence
import time

camera_operator = CameraOperator()

sequence = Sequence(30)

actions = [
    Action(4, camera_operator, "unpause_gameplay"),
    Action(4.5, camera_operator, "power_on"),
    Action(5.5, camera_operator, "start_recording"),
    Action(6, camera_operator.movement_tracker, "start_moving_forward"),
    Action(6, camera_operator.movement_tracker, "start_moving_right"),
    Action(6, camera_operator.movement_tracker, "start_raising"),
    Action(6.5, camera_operator.movement_tracker, "start_rotating_right"),
    Action(10, camera_operator.movement_tracker, "start_lowering"),
    Action(10, camera_operator.movement_tracker, "start_rotating_left"),
    Action(10, camera_operator.movement_tracker, "start_moving_left"),
    Action(15, camera_operator.movement_tracker, "stop_lowering"),
    Action(15, camera_operator.movement_tracker, "stop_moving_left"),
    Action(15, camera_operator.movement_tracker, "stop_rotating_left"),
    Action(17, camera_operator.movement_tracker, "stop_moving_forward"),
    Action(18, camera_operator.movement_tracker, "start_turning_left"),
    Action(20, camera_operator.movement_tracker, "stop_turning_left"),
    Action(23, camera_operator.movement_tracker, "start_zooming_in"),
    Action(24, camera_operator.movement_tracker, "start_zooming_out"),
    Action(25, camera_operator.movement_tracker, "level_out"),
    Action(28, camera_operator, "stop_recording"),
    Action(29, camera_operator, "pause_gameplay"),
    Action(30, camera_operator, "power_off")
]

for action in actions:
    sequence.add_action(action)

print("Starting sequence in 5 seconds")
time.sleep(5)

sequence.run()
