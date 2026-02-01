# Sims 3 Camera Motion Controller


This is a command line tool that acts as a motion controller
for the Sims 3 in-game camera.

## Running the Program
- Navigate to the project in command prompt
- Run `python . --use=(file)`, with file being the YAML file relative to the workspace directory.
  - Example: to run using workspace/demo.yaml, run `python . --use=demo.yaml`
- The program will tell you to open your game window. Do that within 10 seconds of starting he program.
- Once it starts, it will go through the sequence, printing out its current point in the sequence
  and which action it's running, if any. At the end, it will print out a message saying the sequence is finished.

## Configuring Your Own Camera Motion Controls 


The program will look for the camera motion control configuration you want to use
in the workspace directory. It will also expect it to be in proper YAML format.

### Each YAML configuration needs the following:
- `sequence_length_in_seconds`: exactly what it sounds like; **allowed to be on 0.5 second intervals**
- `sequence_actions`: a set of actions that you want to run at certain points in your sequence; requires:
  - `run_at_second_mark`: the point at which you want to action to run in the sequence
  - `action_to_run`: the camera movement or operation you wish to perform at the specified point in the sequence

### Available actions to use in `action_to_run`:

#### Camera Power & Recording
- `power_on` - Puts the game into cameraman mode (i.e., like pressing the Tab key)
- `power_off` - Takes the game out of cameraman mode
- `start_recording` - Starts recording the camera view
- `stop_recording` - Stops recording the camera view
- `take_snapshot` - Takes a single screenshot
- `pause_gameplay` - Pauses the game
- `unpause_gameplay` - Unpauses the game

**Linear Movement:**
- `movement_tracker.start_moving_forward` - Begin moving forward
- `movement_tracker.stop_moving_forward` - Stop moving forward
- `movement_tracker.start_moving_backward` - Begin moving backward
- `movement_tracker.stop_moving_backward` - Stop moving backward
- `movement_tracker.start_moving_left` - Begin moving left
- `movement_tracker.stop_moving_left` - Stop moving left
- `movement_tracker.start_moving_right` - Begin moving right
- `movement_tracker.stop_moving_right` - Stop moving right

**Vertical Movement:**
- `movement_tracker.start_raising` - Begin raising the camera
- `movement_tracker.stop_raising` - Stop raising the camera
- `movement_tracker.start_lowering` - Begin lowering the camera
- `movement_tracker.stop_lowering` - Stop lowering the camera

**Zoom:**
- `movement_tracker.start_zooming_in` - Begin zooming in
- `movement_tracker.stop_zooming_in` - Stop zooming in
- `movement_tracker.start_zooming_out` - Begin zooming out
- `movement_tracker.stop_zooming_out` - Stop zooming out

**Rotation:**
- `movement_tracker.start_rotating_left` - Begin rotating left
- `movement_tracker.stop_rotating_left` - Stop rotating left
- `movement_tracker.start_rotating_right` - Begin rotating right
- `movement_tracker.stop_rotating_right` - Stop rotating right

**Turning:**
- `movement_tracker.start_turning_left` - Begin turning left
- `movement_tracker.stop_turning_left` - Stop turning left
- `movement_tracker.start_turning_right` - Begin turning right
- `movement_tracker.stop_turning_right` - Stop turning right

**Camera Positioning:**
- `movement_tracker.level_out` - Levels the camera to a neutral angle
- `movement_tracker.snap_to_position_5` through `movement_tracker.snap_to_position_9` - Instantly snap to saved camera positions (5-9)
- `movement_tracker.move_to_position_5` through `movement_tracker.move_to_position_9` - Smoothly move to saved camera positions (5-9)

**Utility:**
- `movement_tracker.stop_all_tracked_movements` - Stops all active movements at once

## Important Notes
- This will only work on Windows machines.
- The sequence timing actions on 0.5 second intervals. Anything that isn't at an interval of 0.5 will not run.
- The tracking of sequence time uses the Python Time library's `sleep` function,
  meaning the counting of these increments is not guaranteed to be 100% accurate.
- The program tries to stop movements that are impossible to continue with a newly tracked movement.
  For example, if you tell the camera to move forward, don't tell it top stop, and then tell it to move backward,
  it will try to stop moving forward before it starts moving backward because doing both at once is impossible.