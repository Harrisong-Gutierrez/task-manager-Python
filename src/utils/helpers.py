from datetime import datetime

def format_datetime(dt):
    return dt.strftime("%Y-%m-%d %H:%M")

def parse_priority(priority_str):
    priority_map = {
        '1': 1, 'baja': 1, 'low': 1,
        '2': 2, 'media': 2, 'medium': 2,
        '3': 3, 'alta': 3, 'high': 3
    }
    return priority_map.get(priority_str.lower(), 2)  