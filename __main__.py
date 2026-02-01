from src.processor import Processor
import sys

def main():
    yaml_file = "demo.yaml"
    
    for arg in sys.argv[1:]:
        if arg.startswith("--use="):
            yaml_file = arg.split("=", 1)[1]
    
    processor = Processor(use_workspace_file=yaml_file)
    processor.process()
    

if __name__ == "__main__":
    main()
