import math
from datetime import datetime, timedelta

from endless_2020.constants import END_OF_2020, DAYS_IN_DECEMBER, LAST_SUNDAY_IN_2020, DAYS_IN_A_WEEK, WEEKS_IN_2020, \
    LAST_MONDAY_IN_2020


def get_day_offset(input_date: datetime) -> int:
    """Calculates the number of days since December 31, 2020"""
    delta = input_date - END_OF_2020
    return delta.days


def get_datetime(day_offset: int) -> datetime:
    return END_OF_2020 + timedelta(days=day_offset)


def get_week_number_sunday_first(input_date: datetime) -> int:
    days = get_day_offset(input_date) + DAYS_IN_DECEMBER - LAST_SUNDAY_IN_2020
    return math.floor(days / DAYS_IN_A_WEEK) + WEEKS_IN_2020


def get_week_number_monday_first(input_date: datetime) -> int:
    days = get_day_offset(input_date) + DAYS_IN_DECEMBER - LAST_MONDAY_IN_2020
    return math.floor(days / DAYS_IN_A_WEEK) + WEEKS_IN_2020


def get_week_number_iso_8601(input_date: datetime) -> int:
    return 0
