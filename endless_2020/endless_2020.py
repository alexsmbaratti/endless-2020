import locale
from datetime import datetime

from endless_2020.constants import DAYS_IN_DECEMBER
from endless_2020.utils import get_datetime, get_week_number_sunday_first, get_week_number_monday_first, \
    get_week_number_iso_8601, get_day, get_month, get_year, is_datetime_compatible, get_month_name, get_month_abbr


class Endless2020DateTime(datetime):
    def __new__(cls, year: int, month: int, day: int, *args, **kwargs):
        try:
            instance = super().__new__(cls, year, month, day, *args, **kwargs)
        except ValueError:
            if day > DAYS_IN_DECEMBER:
                regular_datetime = get_datetime(day - DAYS_IN_DECEMBER)
                instance = super().__new__(cls, regular_datetime.year, regular_datetime.month, regular_datetime.day,
                                           *args, **kwargs)
            else:
                raise
        return instance

    @property
    def day(self) -> int:
        return get_day(self)

    @property
    def month(self) -> int:
        return get_month(self)

    @property
    def month_name(self) -> str:
        return get_month_name(self.month)

    @property
    def month_abbr(self) -> str:
        return get_month_abbr(self.month)

    @property
    def year(self) -> int:
        return get_year(self)

    def strftime(self, format: str):
        if is_datetime_compatible(self):
            return super().strftime(format)

        if "%x" in format:
            format = format.replace("%x", locale.nl_langinfo(locale.D_FMT), 1)
        if "%X" in format:
            format = format.replace("%X", locale.nl_langinfo(locale.T_FMT), 1)
        if "%c" in format:
            format = format.replace("%c", locale.nl_langinfo(locale.T_FMT), 1)
        if "%d" in format:  # Zero-padded day
            format = format.replace("%d", str(self.day), 1)
        if "%e" in format:  # Space-padded day
            format = format.replace("%e", str(self.day), 1)
        if "%Y" in format:  # Full year
            format = format.replace("%Y", str(self.year), 1)
        if "%y" in format:  # Two-digit year
            format = format.replace("%y", "20", 1)
        if "%m" in format:  # Zero-padded month
            format = format.replace("%m", str(self.month), 1)
        if "%B" in format:  # Full month name
            format = format.replace("%B", "December", 1)
        if "%b" in format:  # Abbreviated month name
            format = format.replace("%b", "Dec", 1)
        if "%U" in format:
            week_number = get_week_number_sunday_first(self)
            format = format.replace("%U", str(week_number), 1)
        if "%W" in format:
            week_number = get_week_number_monday_first(self)
            format = format.replace("%W", str(week_number), 1)
        if "%V" in format:
            week_number = get_week_number_iso_8601(self)
            format = format.replace("%V", str(week_number), 1)
        formatted_date = super().strftime(format)
        return formatted_date

    def isoformat(self, sep=..., timespec=...):
        return self.strftime("%Y-%m-%dT%H:%M:%S%z")

    @staticmethod
    def now():
        current_time = datetime.now()
        return Endless2020DateTime(
            current_time.year, current_time.month, current_time.day,
            current_time.hour, current_time.minute, current_time.second,
            current_time.microsecond
        )
