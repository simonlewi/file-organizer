from pathlib import Path
import shutil
import logging
from file_utils import *


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def scan_directory(directory_path):
    """
    Scan the directory and return a list of files.
    """
    directory = Path(directory_path)
    files = []

    if not directory.exists() or not directory.is_dir():
        logging.error(f"{directory} is not a valid directory.")
        return files

    try:
        # List all files (not directories) in the given directory
        files = [f for f in directory.iterdir() if f.is_file()]
        logging.info(f"Found {len(files)} files in {directory}.")
    except PermissionError:
        logging.error(f"Permission denied: Cannot access directory {directory}")
    except Exception as e:
        logging.error(f"Error scanning directory {directory}: {e}")

    return files


def create_destination_folders(base_directory, organization_type="extension"):
    """
    Create destination folders based on the organization type.
    """
    base_dir = Path(base_directory)

    if not base_dir.exists():
        logging.error(f"Base directory {base_directory} does not exist.")
        return

    if organization_type == "extension":
        from file_utils import get_file_extension
        folders = list(FILE_EXTENSIONS.keys()) + ["Other"]
    elif organization_type == "size":
        folders = ["Small", "Medium", "Large"]
    elif organization_type == "date":
        folders = []
    else:
        folders = []

    created_folders = {}
    for folder in folders:
        folder_path = base_dir / folder
        try:
            folder_path.mkdir(parents=True, exist_ok=True)
            created_folders[folder] = folder_path
            logging.info(f"Created folder: {folder_path}")
        except Exception as e:
            logging.error(f"Error creating folder {folder_path}: {e}")

        return created_folders


def organize_files(source_directory, organization_type="extension", copy=False, dry_run=False):
    """
    Organize files based on specified criteria.

    Parameters:
    - source_directory: Directory containing files to organize
    - organization_type: How to organize files (by extension, size, or date)
    - copy: If True, copy files instead of moving them
    - dry_run: If True, only show what would be done without making changes

    Returns:
    - Dictionary with statistics about the operation
    """

    source_dir= Path(source_directory)

    if not source_dir.exists() or not source_dir.is_dir():
        logging.error(f"{source_directory} is not a valid directory.")
        return {}
    
    
    # Get all files
    files = scan_directory(source_dir)
    if not files:
        return {"error": "No files found or directory is empty."}
    
    # Create destination folders
    dest_folders = create_destination_folders(source_dir, organization_type)
    if not dest_folders:
        logging.error("No destination folders created.")
        return
    
    stats = {
        "total_files": len(files),
        "organized_files": 0,
        "skipped_files": 0,
        "errors": 0,
    }

    # Process each file
    for file in files:
        try:
            # Determine destination folder based on organization type
            if organization_type == "extension":
                category = get_file_category(file)
                dest_folder = dest_folders.get(category)
                if not dest_folder:
                    dest_folder = source_dir / category
                    dest_folder.mkdir(exist_ok=True)
            elif organization_type == "size":
                size_category = categorize_by_size(file)
                dest_folder = dest_folders.get(size_category)
            elif organization_type == "date":
                date_str = categorize_by_date(file)
                # For date, we may have to create the folder dynamically
                dest_folder = source_dir / date_str
                dest_folder.mkdir(exist_ok=True)
            else:
                logging.error(f"Unknown organization type: {organization_type}")
                stats["errors"] += 1
                continue

            if not dest_folder:
                logging.error(f"No destination folder found for file {file}.")
                stats["skipped_files"] += 1
                continue

            # Destination path
            dest_path = dest_folder / file.name

            # Handle duplicate files
            counter = 1
            original_stem = dest_path.stem
            while dest_path.exists():
                new_name = f"{original_stem}_{counter}{dest_path.suffix}"
                dest_path = dest_folder / new_name
                counter += 1

            # Log what would be done
            operation = "Copying" if copy else "Moving"
            if dry_run:
                logging.info(f"[DRY RUN] Would {operation.lower()} {file} to {dest_path}")
            else:
                # Perform the operation
                if copy:
                    shutil.copy2(file, dest_path)
                    logging.info(f"Copied {file} to {dest_path}")

                else:
                    shutil.move(file, dest_path)
                    logging.info(f"Moved {file} to {dest_path}")

            stats["organized_files"] += 1

        except Exception as e:
            logging.error(f"Error processing file {file}: {e}")
            stats["errors"] += 1
            stats["skipped_files"] += 1

    return stats

