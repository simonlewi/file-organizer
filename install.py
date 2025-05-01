#!/usr/bin/env python3
import os
import shutil
import platform
from pathlib import Path

def install():
    try:
        # Determine home directory and platform
        home = Path.home()
        is_windows = platform.system().lower() == "windows"
        
        # Create installation directory
        install_dir = home / ".local" / "bin" if not is_windows else home / "AppData" / "Local" / "FileOrganizer"
        install_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy all necessary files
        current_dir = Path(__file__).parent
        files_to_copy = ['main.py', 'organizer.py', 'file_utils.py', 'reports.py']
        
        for file in files_to_copy:
            try:
                shutil.copy2(current_dir / file, install_dir)
                print(f"Copied {file} to {install_dir}")
            except Exception as e:
                raise Exception(f"Failed to copy {file}: {str(e)}")
        
        # Create appropriate script
        if is_windows:
            script = install_dir / "organize.bat"
            with open(script, 'w') as f:
                f.write(f'@echo off\npython "{install_dir}/main.py" %*')
            
            # Add to PATH if not already there
            os.system(f'setx PATH "%PATH%;{install_dir}"')
        else:
            script = install_dir / "organize"
            with open(script, 'w') as f:
                f.write(f'#!/bin/bash\npython3 "{install_dir}/main.py" "$@"')
            script.chmod(0o755)  # Make executable
            
            # Add to PATH if not already there
            bashrc = home / ".bashrc"
            with open(bashrc, 'a') as f:
                f.write(f'\nexport PATH="$PATH:{install_dir}"\n')

    except Exception as e:
        print(f"Installation failed: {str(e)}")
        return False
    
    return True

if __name__ == "__main__":
    if install():
        print("Installation complete! Please restart your terminal.")
    else:
        exit(1)