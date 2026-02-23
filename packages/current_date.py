import re
from datetime import datetime


d = datetime.now()

# print({d})

date = d.strftime("%d")
# month = d.strftime("%B").lower()
# year = d.strftime("%Y")

# add ordinal suffix (for general integers)
# def ordinal(n):
#     return str(n) + ("th" if 11 <= n % 100 <= 13 else {1:"st",2:"nd",3:"rd"}.get(n % 10, "th"))

def ordinal(n):
    """this is ordinal function to convert integer to ordinal string for day of month"""
    if 10 <= n <= 20:
        suffix = "th"
    else:
        suffix = {1:"st",2:"nd",3:"rd"}.get(n % 10, "th")
    return f"{n}{suffix}"

def normalize_date(date):
    if isinstance(date, int):
        return ordinal(date)

    elif isinstance(date, str):
        date = date.strip()

        # If it's purely numeric like "16"
        if date.isdigit():
            return ordinal(int(date))

        # Handle cases like "17th", "23rd"
        match = re.match(r'^(\d+)(st|nd|rd|th)?$', date.lower())
        if match:
            return ordinal(int(match.group(1)))

        raise ValueError(f"Invalid date format: {date}")

    else:
        raise TypeError("date must be int or str")

date = ordinal(int(date))
month = d.strftime("%B").lower()
year = d.strftime("%Y")
