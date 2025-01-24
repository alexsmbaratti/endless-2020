from datetime import datetime

from endless_2020.constants import END_OF_2020


def get_day_offset(input_date: datetime) -> int:
    """Calculates the number of days since December 31, 2020"""
    delta = input_date - END_OF_2020
    return delta.days
