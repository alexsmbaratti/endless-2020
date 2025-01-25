import locale
from datetime import datetime

from endless_2020.constants import DAYS_IN_DECEMBER
from endless_2020.utils import get_day_offset, get_datetime


class Endless2020DateTime(datetime):
    def __new__(cls, year: int, month: int, day: int, *args, **kwargs):
        try:
            instance = super().__new__(cls, year, month, day, *args, **kwargs)
        except ValueError:
            regular_datetime = get_datetime(day - DAYS_IN_DECEMBER)
            instance = super().__new__(cls, regular_datetime.year, regular_datetime.month, regular_datetime.day)
        return instance

    def strftime(self, format: str):
        day_offset = get_day_offset(self)
        if day_offset <= 0:
            return super().strftime(format)

        day = day_offset + DAYS_IN_DECEMBER
        if "%x" in format:
            format = format.replace("%x", locale.nl_langinfo(locale.D_FMT), 1)
        if "%X" in format:
            format = format.replace("%X", locale.nl_langinfo(locale.T_FMT), 1)
        if "%c" in format:
            format = format.replace("%c", locale.nl_langinfo(locale.T_FMT), 1)
        if "%d" in format:
            format = format.replace("%d", str(day), 1)
        if "%e" in format:
            format = format.replace("%e", str(day), 1)
        if "%Y" in format:
            format = format.replace("%Y", "2020", 1)
        if "%y" in format:
            format = format.replace("%y", "20", 1)
        if "%m" in format:
            format = format.replace("%m", "12", 1)
        if "%B" in format:
            format = format.replace("%B", "December", 1)
        if "%b" in format:
            format = format.replace("%b", "Dec", 1)
        if "%V" in format:
            raise UnsupportedDirectiveException("%V")
        formatted_date = super().strftime(format)
        return formatted_date

    def isoformat(self, sep = ..., timespec = ...):
        return self.strftime("%Y-%m-%dT%H:%M:%S%z")


class UnsupportedDirectiveException(Exception):
    """Exception raised for operations or features that are not supported."""

    def __init__(self, directive: str, *args):
        super().__init__(f"{directive} is not currently supported", *args)
