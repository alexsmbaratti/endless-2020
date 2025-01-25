import math
from datetime import datetime, timedelta

from endless_2020.constants import LAST_DAY_OF_2020, DAYS_IN_DECEMBER, LAST_SUNDAY_IN_2020, DAYS_IN_A_WEEK, \
    WEEKS_IN_2020, LAST_MONDAY_IN_2020


def get_day_offset(input_date: datetime) -> int:
    """Calculates the number of days since December 31, 2020"""
    delta = input_date - LAST_DAY_OF_2020
    return delta.days


def get_day(input_date: datetime) -> int:
    if is_datetime_compatible(input_date):
        return input_date.day

    day_offset = get_day_offset(input_date)
    return day_offset + DAYS_IN_DECEMBER


def get_month(input_date: datetime) -> int:
    if is_datetime_compatible(input_date):
        return input_date.month

    return 12


def get_year(input_date: datetime) -> int:
    if is_datetime_compatible(input_date):
        return input_date.year

    return 2020


def is_datetime_compatible(input_date: datetime) -> bool:
    return input_date <= LAST_DAY_OF_2020


def get_datetime(day_offset: int) -> datetime:
    return LAST_DAY_OF_2020 + timedelta(days=day_offset)


def get_week_number_sunday_first(input_date: datetime) -> int:
    days = get_day_offset(input_date) + DAYS_IN_DECEMBER - LAST_SUNDAY_IN_2020
    return math.floor(days / DAYS_IN_A_WEEK) + WEEKS_IN_2020


def get_week_number_monday_first(input_date: datetime) -> int:
    days = get_day_offset(input_date) + DAYS_IN_DECEMBER - LAST_MONDAY_IN_2020
    return math.floor(days / DAYS_IN_A_WEEK) + WEEKS_IN_2020


def get_week_number_iso_8601(input_date: datetime) -> int:
    return get_week_number_monday_first(input_date)
