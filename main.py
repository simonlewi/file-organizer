import argparse
import os

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
    if not os.path.exists(target_dir):
        print(f"Directory {target_dir} does not exist.")
        return
    
    if os.path.isdir(target_dir):
        print(f"Target directory '{target_dir}' already exists")
    else:
        try:
            os.makedirs(target_dir)
            print(f"Created directory '{target_dir}'")
        except OSError as e:
            print(f"Error creating directory '{target_dir}': {e}")
            return

        
        