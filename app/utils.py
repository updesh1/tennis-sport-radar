def format_number(value):
    return f"{value:,}"

def safe_percentage(part, total):
    return round((part / total) * 100, 1) if total else 0.0
