#!/usr/bin/env python3
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

    try:
        print(f"Organizing files in '{directory}' by {args.org_type}...")
        if args.dry_run:
            print("DRY RUN MODE: No changes will be made.")
                        
        stats = organize_files(
            args.directory,
            organization_type=args.org_type,
            copy=args.copy,
            dry_run=args.dry_run
        )
        
        if not stats:
            print("\nError: Organization failed.")
            return 1
            
        if stats.get("status") == "empty":
            print(f"\nDone! No files to organize")
            return 0
            
        if stats.get("status") == "error":
            print(f"\nError: {stats.get('error_message', 'Unknown error occurred')}")
            return 1
            
        # Print success message
        if stats.get('organized_files', 0) > 0:
            print(f"\nDone! Organized {stats.get('organized_files', 0)} files.")
            if stats.get('skipped_files', 0) > 0:
                print(f"Skipped {stats['skipped_files']} files.")
            if stats.get('errors', 0) > 0:
                print(f"Encountered {stats['errors']} errors.")
        else:
            print(f"\nDone! No files to organize")
            
        if args.report:
            print("\n" + generate_report(stats, directory, args.org_type))       
            
        return 0
        
    except Exception as e:
        print(f"\nError: {str(e)}")
        return 1

if __name__ == "__main__":
    exit(main())

        
        