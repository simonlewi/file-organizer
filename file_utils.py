import mimetypes
import os
from pathlib import Path
import logging

FILE_EXTENSIONS = {
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx", ".csv", ".xml", ".json"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".go"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
}

MIME_CATEGORIES = {
    "image/": "Images",
    "audio/": "Audio",
    "video/": "Videos",
    "application/pdf": "Documents",
    "application/msword": "Documents",
    "application/vnd.openxmlformats-officedocument": "Documents",
    "text/": "Documents",
    "application/zip": "Archives",
    "application/x-rar": "Archives",
    "application/x-tar": "Archives",
    "application/gzip": "Archives",
}

mimetypes.init()
mimetypes.add_type('.mp3', '.wav')

def get_category_by_extension(extension):
    """Return the category for a given file extension."""
    extension = extension.lower() # Convert to lowercase for case insensitivity
    for category, extensions in FILE_EXTENSIONS.items():
        if extension in extensions:
            return category
    return "Other" # Default category for uncategorized files
    
def get_file_category(file_path):
    """
    Determine a file's category using MIME type first, then extension as fallback.
    """
    # Try file command first (for Linux systems)
    if os.name != "nt":
        try:
            import subprocess
            result = subprocess.run(['file', '--mime-type', '-b', str(file_path)], 
                                 capture_output=True, text=True)
            detected_mime = result.stdout.strip()
            
            if detected_mime:
                for mime_prefix, category in MIME_CATEGORIES.items():
                    if detected_mime.startswith(mime_prefix):
                        return category
        except Exception as e:
            logging.error(f"Error using file command: {e}")
    
    # Then try mimetypes library
    mime_type, _ = mimetypes.guess_type(str(file_path))
    if mime_type:
        for mime_prefix, category in MIME_CATEGORIES.items():
            if mime_type.startswith(mime_prefix):
                return category

    # Use extension as last resort
    ext = get_file_extension(file_path)
    if ext:
        # Check common extensions first
        if ext.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']:
            return "Images"
        elif ext.lower() in ['.mp3', '.wav', '.aac', '.flac', '.m4a']:
            return "Audio"
        elif ext.lower() in ['.mp4', '.mkv', '.avi', '.mov', '.wmv']:
            return "Videos"
        
        # Then check FILE_EXTENSIONS dictionary
        category = get_category_by_extension(ext)
        if category != "Other":
            return category

    return "Other"
    
def get_file_extension(filename):
    """Extract the extension from a filename."""
    from pathlib import Path
    return Path(filename).suffix.lower()

def is_categorized(extension):
    """Check if a file extension is categorized"""
    extension = extension.lower()
    return any(extension in exts for exts in FILE_EXTENSIONS.values())

def categorize_by_size(file_path):
    """Categorize files by size."""
    from pathlib import Path
    size_bytes = Path(file_path).stat().st_size
    if size_bytes < 1024 * 1024:  # Less than 1 MB
        return "Small"
    elif size_bytes < 100 * 1024 * 1024:  # Less than 100 MB
        return "Medium"
    else:
        return "Large"
    
def categorize_by_date(file_path):
    """Categorize files by creation date."""
    from pathlib import Path
    from datetime import datetime

    # Make sure the file_path is a Path object
    path = Path(file_path) if not isinstance(file_path, Path) else file_path

    creation_time = path.stat().st_ctime
    creation_date = datetime.fromtimestamp(creation_time)
    return creation_date.strftime("%Y-%m")


