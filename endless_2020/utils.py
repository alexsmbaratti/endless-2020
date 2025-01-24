from datetime import datetime, timedelta

from endless_2020.constants import END_OF_2020


def get_day_offset(input_date: datetime) -> int:
    """Calculates the number of days since December 31, 2020"""
    delta = input_date - END_OF_2020
    return delta.days


def get_datetime(day_offset: int) -> datetime:
    return END_OF_2020 + timedelta(days=day_offset)
