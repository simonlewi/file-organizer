# File Organizer

A command-line tool to organize files by type, date, or size. Supports both Windows and Linux systems.

## Features

- Organize files by:
  - Type/Extension (default)
  - Date
  - Size
- Support for common file types (documents, images, audio, video, archives)
- MIME type detection for accurate file categorization
- Optional file copying instead of moving
- Dry run mode to preview changes
- Detailed operation reports

(Create your own organization config coming in later version)

## Installation Guide

### Prerequisites
Before installing, make sure you have:
1. Python 3.6 or higher installed
   - To check, open terminal and type: `python3 --version`
   - If not installed, visit [Python's official website](https://www.python.org/downloads/)

### Linux Installation (Ubuntu/Debian)

**Method 1: Simple Script Installation (Recommended)**
1. Open Terminal (Press `Ctrl + Alt + T`)
2. Navigate to the downloaded folder:
   ```bash
   cd path/to/file-organizer
   ```
3. Make the install script executable:
   ```bash
   chmod +x scripts/install.sh
   ```
4. Run the installation:
   ```bash
   ./scripts/install.sh
   ```
5. Restart your terminal or run:
   ```bash
   source ~/.bashrc
   ```

**Method 2: Python Installation**
1. Open Terminal
2. Navigate to the downloaded folder
3. Run:
   ```bash
   python3 install.py
   ```

### Windows Installation

1. Open Command Prompt as Administrator
   - Press `Win + X`
   - Click "Windows PowerShell (Admin)" or "Command Prompt (Admin)"
2. Navigate to the downloaded folder:
   ```cmd
   cd path\to\file-organizer
   ```
3. Run the installer:
   ```cmd
   python install.py
   ```
4. Close and reopen Command Prompt

### Verifying Installation

To verify the installation was successful:
1. Open a new terminal/command prompt
2. Type:
   ```bash
   organize --help
   ```
3. You should see the help message with available options

### Troubleshooting

**Common Issues:**

1. "Command not found" error
   - Solution: Make sure you restarted your terminal after installation

2. "Permission denied" error
   - Linux Solution: Run `chmod +x scripts/install.sh`
   - Windows Solution: Run Command Prompt as Administrator

3. "Python not found" error
   - Make sure Python is installed and added to your system PATH
   - Try using `python3` instead of `python` on Linux

Need help? [Create an issue](https://github.com/yourusername/file-organizer/issues)

## Usage

Basic usage:
```bash
organize /path/to/directory
```

Options:
```bash
organize /path/to/directory [options]

Options:
  --by-type     Organize by file type (default)
  --by-date     Organize by creation date
  --by-size     Organize by file size
  --copy        Copy files instead of moving them
  --dry-run     Show what would be done without making changes
  --report      Generate a detailed report after organizing
```

### Examples

1. Organize current directory by file type:
```bash
organize .
```

2. Organize downloads folder by date with report:
```bash
organize ~/Downloads --by-date --report
```

3. Preview organization by size:
```bash
organize ~/Documents --by-size --dry-run
```

4. Copy files instead of moving them:
```bash
organize ~/Pictures --copy
```

## Supported File Types

- Documents: .pdf, .docx, .txt, .pptx, .xlsx, .csv, .xml, .json
- Images: .jpg, .jpeg, .png, .gif, .bmp, .tiff, .svg, .webp
- Audio: .mp3, .wav, .aac, .flac
- Video: .mp4, .mkv, .avi, .mov
- Archives: .zip, .rar, .tar, .gz
- Code: .py, .js, .html, .css, .java, .c, .cpp, .go

## Requirements

- Python 3.6 or higher
- Linux or Windows operating system

## Uninstallation

### Linux
```bash
rm -rf ~/.local/bin/organize ~/.local/bin/main.py ~/.local/bin/organizer.py ~/.local/bin/file_utils.py ~/.local/bin/reports.py
```

### Windows
```bash
rd /s /q "%USERPROFILE%\AppData\Local\FileOrganizer"
```

## License

MIT License