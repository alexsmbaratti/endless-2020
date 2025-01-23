from datetime import datetime
from endless_2020.constants import END_OF_2020


def get_day_offset(input_date: datetime) -> int:
    """Calculates the number of days since December 31, 2020"""
    delta = input_date - END_OF_2020
    return delta.days


def strftime(input_date: datetime, fmt: str = "%Y-%m-%d %H:%M:%S.%f") -> str:
    if input_date < END_OF_2020:
        return input_date.strftime(fmt)

    day_offset = get_day_offset(input_date) + 31
    if "%d" in fmt:
        fmt = fmt.replace("%d", str(day_offset), 1)
    if "%e" in fmt:
        fmt = fmt.replace("%e", str(day_offset), 1)
    if "%Y" in fmt:
        fmt = fmt.replace("%Y", "2020", 1)
    if "%m" in fmt:
        fmt = fmt.replace("%m", "12", 1)
    if "%B" in fmt:
        fmt = fmt.replace("%B", "December", 1)
    formatted_date = input_date.strftime(fmt)
    return formatted_date
