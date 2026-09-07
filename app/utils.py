def format_number(value):
    """Format a number with commas."""
    return f"{int(value):,}"


def safe_percentage(part, total):
    """Calculate a percentage safely."""
    return round((part / total) * 100, 1) if total else 0.0