import argparse
import os
from pathlib import Path
from organizer import organize_files
from reports import generate_report

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Organize files in a directory by type, date or size."
    )
    
    parser.add_argument(
        "directory", 
        help="Directory path to organize"
    )
    
    parser.add_argument(
        "--by-type", 
        dest="org_type", 
        action="store_const",
        const="extension",
        default="extension", 
        help="Organize files by type (default)"
    )

    parser.add_argument(
        "--by-date",
        dest="org_type",
        action="store_const",
        const="date",
        help="Organize files by date"
    )

    parser.add_argument(
        "--by-size",
        dest="org_type",
        action="store_const",
        const="size",
        help="Organize files by size"
    )

    parser.add_argument(
        "--copy",
        action="store_true",
        help="Copy files instead of moving them"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without making changes"
    )

    parser.add_argument(
        "--report",
        action="store_true",
        help="Generate a report after organizing files"
    )

    # Parse aguments
    args = parser.parse_args()

    # Process the directory
    directory = args.directory

    if not os.path.exists(directory):
        print(f"Error: '{directory}' is not a valid directory.")
        return 1
    
    print(f"Organizing files in '{directory}' by {args.org_type}...")
    if args.dry_run:
        print("DRY RUN MODE: No changes will be made.")

    stats = organize_files(
        directory, 
        organization_type=args.org_type,
        copy=args.copy,
        dry_run=args.dry_run
    )

    if args.report:
        report = generate_report(stats, directory, args.org_type)
        print("\n" + report)
    else:
        print(f"\nDone! Organized {stats['organized_files']} files.")
        if stats['errors'] > 0:
            print(f"Encountered {stats['errors']} errors. Check the logs for details.")

    return 0

if __name__ == "__main__":
    exit(main())

        
        