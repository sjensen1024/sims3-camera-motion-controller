from src.camera.camera_operator import CameraOperator
from src.motion_control.action import Action
from src.motion_control.sequence import Sequence
import time
import sys
import yaml
from pathlib import Path
from functools import reduce

def load_sequence_config_from_yaml(yaml_file: str) -> dict:
    workspace_dir = Path(__file__).parent / "workspace"
    yaml_path = workspace_dir / yaml_file
    
    if not yaml_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {yaml_path}")
    
    with open(yaml_path, 'r') as f:
        config = yaml.safe_load(f)
    
    return config


def resolve_action_path(camera_operator: CameraOperator, path: str):
    parts = path.split('.')
    return reduce(getattr, parts, camera_operator)


def create_sequence_from_config(config: dict, camera_operator: CameraOperator) -> Sequence:
    sequence_length = config.get('sequence_length_in_seconds')
    sequence = Sequence(sequence_length)
    
    for action_config in config.get('sequence_actions', []):
        run_at_second_mark = action_config.get('run_at_second_mark')
        action_to_run_path = action_config.get('action_to_run')
        
        if run_at_second_mark is None or action_to_run_path is None:
            raise ValueError(f"Invalid action config: {action_config}")
        
        action_callable = resolve_action_path(camera_operator, action_to_run_path)
        action = Action(run_at_second_mark, action_callable)
        sequence.add_action(action)
    
    return sequence


def main():
    yaml_file = "demo.yaml"
    
    for arg in sys.argv[1:]:
        if arg.startswith("--use="):
            yaml_file = arg.split("=", 1)[1]
    
    camera_operator = CameraOperator()
    config = load_sequence_config_from_yaml(yaml_file)
    sequence = create_sequence_from_config(config, camera_operator)
    print(f"Open your game window. The sequence from workspace/{yaml_file} will start in 10 seconds.")
    time.sleep(10)
    sequence.run()

if __name__ == "__main__":
    main()
