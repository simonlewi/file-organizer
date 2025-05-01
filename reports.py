def generate_report(stats, source_directory, organization_type):
    """
    Generate a report of the organization process.
    """
    report = []
    report.append(f"File Organization Report")
    report.append(f"========================")
    report.append(f"Source Directory: {source_directory}")
    report.append(f"Organization Type: {organization_type}")
    report.append(f"Total Files: {stats['total_files']}")
    report.append(f"Files Organized: {stats['organized_files']}")
    report.append(f"Files Skipped: {stats['skipped_files']}")
    report.append(f"Errors: {stats['errors']}")
    report.append(f"========================")

    return "\n".join(report)



