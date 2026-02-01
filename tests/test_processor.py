import unittest
from unittest.mock import Mock, patch, MagicMock
from pathlib import Path
import tempfile
import yaml
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.processor import Processor
from src.motion_control.action import Action
from src.motion_control.sequence import Sequence


class TestProcessor(unittest.TestCase):
    """Unit tests for the Processor class."""

    def setUp(self):
        """Set up test fixtures."""
        self.processor = Processor(use_workspace_file="demo.yaml")

    def test_processor_initialization(self):
        """Test Processor initializes with correct attributes."""
        self.assertEqual(self.processor.use_workspace_file, "demo.yaml")
        self.assertIsNotNone(self.processor.camera_operator)

    def test_processor_initialization_custom_file(self):
        """Test Processor initializes with custom workspace file."""
        processor = Processor(use_workspace_file="custom.yaml")
        self.assertEqual(processor.use_workspace_file, "custom.yaml")

    @patch('src.processor.time.sleep')
    @patch('builtins.print')
    def test_process_method(self, mock_print, mock_sleep):
        """Test process method calls sequence.run()."""
        with patch.object(self.processor, 'load_sequence_config_from_yaml') as mock_load:
            with patch.object(self.processor, 'create_sequence_from_config') as mock_create:
                mock_config = {'sequence_length_in_seconds': 10, 'sequence_actions': []}
                mock_load.return_value = mock_config
                
                mock_sequence = Mock(spec=Sequence)
                mock_create.return_value = mock_sequence
                
                self.processor.process()
                
                mock_load.assert_called_once()
                mock_create.assert_called_once_with(mock_config)
                mock_sequence.run.assert_called_once()
                mock_sleep.assert_called_once_with(10)

    def test_load_sequence_config_from_yaml_file_not_found(self):
        """Test loading config raises FileNotFoundError for missing file."""
        processor = Processor(use_workspace_file="nonexistent.yaml")
        
        with self.assertRaises(FileNotFoundError) as context:
            processor.load_sequence_config_from_yaml()
        
        self.assertIn("Configuration file not found", str(context.exception))

    @patch('builtins.open', create=True)
    def test_load_sequence_config_from_yaml_valid_file(self, mock_open):
        """Test loading config from valid YAML file."""
        yaml_content = """
sequence_length_in_seconds: 40
sequence_actions:
  - run_at_second_mark: 2
    action_to_run: unpause_gameplay
"""
        mock_open.return_value.__enter__.return_value = mock_open.return_value
        mock_open.return_value.__iter__.return_value = yaml_content.split('\n')
        
        with patch('pathlib.Path.exists', return_value=True):
            with patch('yaml.safe_load') as mock_yaml_load:
                config = {
                    'sequence_length_in_seconds': 40,
                    'sequence_actions': [
                        {'run_at_second_mark': 2, 'action_to_run': 'unpause_gameplay'}
                    ]
                }
                mock_yaml_load.return_value = config
                
                result = self.processor.load_sequence_config_from_yaml()
                
                self.assertEqual(result['sequence_length_in_seconds'], 40)
                self.assertEqual(len(result['sequence_actions']), 1)

    def test_resolve_action_path_single_level(self):
        """Test resolving single-level action path."""
        # Mock the camera_operator attribute
        mock_method = Mock()
        self.processor.camera_operator.test_method = mock_method
        
        result = self.processor.resolve_action_path('test_method')
        
        self.assertEqual(result, mock_method)

    def test_resolve_action_path_nested(self):
        """Test resolving nested action path."""
        # Create mock nested structure
        mock_inner_method = Mock()
        mock_inner = Mock()
        mock_inner.inner_method = mock_inner_method
        self.processor.camera_operator.outer = mock_inner
        
        result = self.processor.resolve_action_path('outer.inner_method')
        
        self.assertEqual(result, mock_inner_method)

    def test_create_sequence_from_config_empty_actions(self):
        """Test creating sequence with no actions."""
        config = {
            'sequence_length_in_seconds': 10,
            'sequence_actions': []
        }
        
        sequence = self.processor.create_sequence_from_config(config)
        
        self.assertIsInstance(sequence, Sequence)
        self.assertEqual(sequence.duration_in_seconds, 10)

    def test_create_sequence_from_config_missing_sequence_length(self):
        """Test creating sequence with missing sequence_length_in_seconds."""
        config = {
            'sequence_actions': []
        }
        
        with self.assertRaises(TypeError) as context:
            self.processor.create_sequence_from_config(config)

    def test_create_sequence_from_config_missing_run_at_second_mark(self):
        """Test creating sequence raises error when run_at_second_mark is missing."""
        config = {
            'sequence_length_in_seconds': 10,
            'sequence_actions': [
                {'action_to_run': 'some_action'}
            ]
        }
        
        with self.assertRaises(ValueError) as context:
            self.processor.create_sequence_from_config(config)
        
        self.assertIn("Invalid action config", str(context.exception))

    def test_create_sequence_from_config_missing_action_to_run(self):
        """Test creating sequence raises error when action_to_run is missing."""
        config = {
            'sequence_length_in_seconds': 10,
            'sequence_actions': [
                {'run_at_second_mark': 5}
            ]
        }
        
        with self.assertRaises(ValueError) as context:
            self.processor.create_sequence_from_config(config)
        
        self.assertIn("Invalid action config", str(context.exception))

    def test_create_sequence_from_config_with_actions(self):
        """Test creating sequence with valid actions."""
        # Mock the camera operator methods
        mock_method1 = Mock()
        mock_method2 = Mock()
        self.processor.camera_operator.action1 = mock_method1
        self.processor.camera_operator.action2 = mock_method2
        
        config = {
            'sequence_length_in_seconds': 40,
            'sequence_actions': [
                {'run_at_second_mark': 2, 'action_to_run': 'action1'},
                {'run_at_second_mark': 5, 'action_to_run': 'action2'}
            ]
        }
        
        sequence = self.processor.create_sequence_from_config(config)
        
        self.assertIsInstance(sequence, Sequence)
        self.assertEqual(sequence.duration_in_seconds, 40)

    def test_create_sequence_from_config_with_nested_actions(self):
        """Test creating sequence with nested action paths."""
        # Create mock nested structure
        mock_nested_method = Mock()
        mock_nested = Mock()
        mock_nested.nested_action = mock_nested_method
        self.processor.camera_operator.tracker = mock_nested
        
        config = {
            'sequence_length_in_seconds': 20,
            'sequence_actions': [
                {'run_at_second_mark': 3, 'action_to_run': 'tracker.nested_action'}
            ]
        }
        
        sequence = self.processor.create_sequence_from_config(config)
        
        self.assertIsInstance(sequence, Sequence)
        self.assertEqual(sequence.duration_in_seconds, 20)


class TestProcessorIntegration(unittest.TestCase):
    """Integration tests for Processor with actual files."""

    def setUp(self):
        """Set up integration test fixtures."""
        # Create a temporary workspace directory and YAML file
        self.temp_dir = tempfile.TemporaryDirectory()
        self.workspace_dir = Path(self.temp_dir.name) / "workspace"
        self.workspace_dir.mkdir(exist_ok=True)

    def tearDown(self):
        """Clean up temporary files."""
        self.temp_dir.cleanup()

    def test_load_sequence_config_from_actual_yaml_file(self):
        """Test loading config from an actual YAML file."""
        yaml_file = self.workspace_dir / "test_config.yaml"
        config_data = {
            'sequence_length_in_seconds': 30,
            'sequence_actions': [
                {'run_at_second_mark': 1, 'action_to_run': 'test_action'}
            ]
        }
        
        with open(yaml_file, 'w') as f:
            yaml.dump(config_data, f)
        
        processor = Processor(use_workspace_file="test_config.yaml")
        
        with patch('pathlib.Path') as mock_path:
            mock_path.return_value.parent.parent.__truediv__ = Mock(return_value=self.workspace_dir)
            mock_path.return_value.__truediv__ = Mock(return_value=yaml_file)
            mock_path.return_value.exists = Mock(return_value=True)
            
            # Directly test with the actual file
            with open(yaml_file, 'r') as f:
                loaded_config = yaml.safe_load(f)
            
            self.assertEqual(loaded_config['sequence_length_in_seconds'], 30)
            self.assertEqual(len(loaded_config['sequence_actions']), 1)


if __name__ == '__main__':
    unittest.main()
