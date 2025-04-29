import argparse
import os
from pathlib import Path

def setup_argument_parser():
    parser = argparse.ArgumentParser(
        description="Organize files in a directory."
        )
    parser.add_argument(
        "directory", 
        type=str, 
        help="Directory to organize"
        )
    parser.add_argument(
        "--by-type", 
        type=str, 
        nargs='+', 
        help="Organize files by type")
    
    return parser.parse_args()

def main():
    # Get command line arguments
    args = setup_argument_parser()

    # Use directory path from arguments
    target_dir = args.directory
    target_path = Path(target_dir)

    # Check if the directory exists
    if not os.path.exists(target_dir):
        print(f"Directory {target_dir} does not exist.")
        return
    
    # Create the target directory if it doesn't exist
    if target_path.is_dir():
        print(f"Target directory '{target_path}' already exists")
    else:
        try:
            target_path.mkdir(parents=True, exist_ok=True)
            print(f"Created directory: {target_path}")
        except Exception as e:
            print(f"Error creating directory '{target_path}': {e}")
            return

        
        