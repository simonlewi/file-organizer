FILE_EXTENSIONS = {
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
}

def get_category_by_extension(extension):
    extension = FILE_EXTENSIONS.lower() # Convert to lowercase for case insensitivity
    for category, extensions in FILE_EXTENSIONS.items():
        if extension in extensions:
            return category
        return "Other" # Default category for uncategorized files
    
def get_file_extension(filename):
    from pathlib import Path
    return Path(filename).suffix.lower()

def is_categorized(extension):
    # Check if a file extension is categorized
    extension = FILE_EXTENSIONS.lower()
    return any(extension in exts for exts in FILE_EXTENSIONS.values())

def categorize_by_size(file_path):
    # Categorize files by size
    from pathlib import Path
    size_bytes = Path(file_path).stat().st_size
    if size_bytes < 1024 * 1024:  # Less than 1 MB
        return "Small"
    elif size_bytes < 100 * 1024 * 1024:  # Less than 10 MB
        return "Medium"
    else:
        return "Large"
    
def categorize_by_date(file_path):
    # Categorize files by date
    from pathlib import Path
    from datetime import datetime

    # Make sure the file_path is a Path object
    path = Path(file_path) if not isinstance(file_path, Path) else file_path

    creation_time = path.stat().st_ctime
    creation_date = datetime.fromtimestamp(creation_time)
    return creation_date.strftime("%Y-%m-%d")


