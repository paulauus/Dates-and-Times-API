"""Functions for working with dates."""

from datetime import datetime, date


def convert_to_datetime(date_val: str) -> datetime:
    """Converts a dd.mm.yyyy input into a datetime object."""
    try:
        return datetime.strptime(date_val, "%d.%m.%Y")
    except ValueError:
        raise ValueError("Unable to convert value to datetime.")


def get_days_between(first: datetime, last: datetime) -> int:
    """Calculates the no. of days between given dates."""
    if not isinstance(first, datetime) or not isinstance(last, datetime):
        raise TypeError("Datetimes required.")
    answer = (last - first).days
    return answer


def get_day_of_week_on(date_val: datetime) -> str:
    """Outputs the day of the week of a given date."""
    if not isinstance(date_val, datetime):
        raise TypeError("Datetime required.")
    days_of_week = ["Monday", "Tuesday", "Wednesday",
                    "Thursday", "Friday", "Saturday", "Sunday"]
    answer = date_val.weekday()
    return days_of_week[answer]


def get_current_age(birthdate: date) -> int:
    """Returns a person's age based on birthdate."""
    if not isinstance(birthdate, date):
        raise TypeError("Date required.")
    today = date.today()
    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age
