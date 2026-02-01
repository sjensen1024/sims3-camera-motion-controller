from src.camera.camera_operator import CameraOperator
from src.motion_control.action import Action
from src.motion_control.sequence import Sequence
import time
import yaml
from pathlib import Path
from functools import reduce

class Processor:
    def __init__(self, use_workspace_file: str = "demo.yaml"):
        self.camera_operator = CameraOperator()
        self.use_workspace_file = use_workspace_file

    def process(self): 
        config = self.load_sequence_config_from_yaml()
        sequence = self.create_sequence_from_config(config)
        print(f"Open your game window. The sequence from workspace/{self.use_workspace_file} will start in 10 seconds.")
        time.sleep(10)
        sequence.run()

    def load_sequence_config_from_yaml(self) -> dict:
        workspace_dir = Path(__file__).parent.parent / "workspace"
        yaml_path = workspace_dir / self.use_workspace_file
        
        if not yaml_path.exists():
            raise FileNotFoundError(f"Configuration file not found: {yaml_path}")
        
        with open(yaml_path, 'r') as f:
            config = yaml.safe_load(f)
        
        return config


    def resolve_action_path(self, path: str):
        parts = path.split('.')
        return reduce(getattr, parts, self.camera_operator)


    def create_sequence_from_config(self, config: dict) -> Sequence:
        sequence_length = config.get('sequence_length_in_seconds')
        sequence = Sequence(sequence_length)
        
        for action_config in config.get('sequence_actions', []):
            run_at_second_mark = action_config.get('run_at_second_mark')
            action_to_run_path = action_config.get('action_to_run')
            
            if run_at_second_mark is None or action_to_run_path is None:
                raise ValueError(f"Invalid action config: {action_config}")
            
            action_callable = self.resolve_action_path(action_to_run_path)
            action = Action(run_at_second_mark, action_callable)
            sequence.add_action(action)
        
        return sequence
    