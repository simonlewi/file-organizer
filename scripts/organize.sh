#!/bin/bash

#Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PARENT_DIR="$(dirname "$SCRIPT_DIR")"

# Run the main.py script with all passed arguments
python3 "$PARENT_DIR/main.py" "$@"