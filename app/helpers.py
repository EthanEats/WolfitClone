from datetime import datetime


def less_than_day(second_diff):
    if second_diff < 10:
        return "just now"
    if second_diff < 60:
        return str(second_diff) + " seconds ago"
    if second_diff < 120:
        return "a minute ago"
    if second_diff < 3600:
        return str(second_diff // 60) + " minutes ago"
    if second_diff < 7200:
        return "an hour ago"
    return str(second_diff // 3600) + " hours ago"


def pretty_date(time=False):
    """
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc
    """
    now = datetime.utcnow()
    if type(time) is int:
        diff = now - datetime.fromtimestamp(time)
    elif isinstance(time, datetime):
        diff = now - time
    elif not time:
        diff = now - now
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return "just about now"

    if day_diff == 0:
        return less_than_day(second_diff)
    if day_diff == 1:
        return "Yesterday"
    if day_diff < 7:
        return str(day_diff) + " days ago"
    if day_diff < 31:
        return str(day_diff // 7) + " weeks ago"
    if day_diff < 365:
        return str(day_diff // 30) + " months ago"
    return str(day_diff // 365) + " years ago"
