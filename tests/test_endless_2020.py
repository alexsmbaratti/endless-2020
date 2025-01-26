import locale
import unittest

from endless_2020.endless_2020 import Endless2020DateTime
from freezegun import freeze_time


class TestEndless2020DateTime(unittest.TestCase):

    def test_init(self):
        timestamp = Endless2020DateTime(2021, 1, 1, hour=18, minute=25, second=3, microsecond=5)
        self.assertEqual("2020-12-32 18:25:03.000005", timestamp.strftime("%Y-%m-%d %H:%M:%S.%f"))
        self.assertEqual(2020, timestamp.year)
        self.assertEqual(12, timestamp.month)
        self.assertEqual(32, timestamp.day)
        self.assertEqual(18, timestamp.hour)
        self.assertEqual(25, timestamp.minute)
        self.assertEqual(3, timestamp.second)
        self.assertEqual(5, timestamp.microsecond)

    def test_init_with_endless_format(self):
        timestamp = Endless2020DateTime(2020, 12, 32)
        self.assertEqual("2020-12-32 00:00:00.000000", timestamp.strftime("%Y-%m-%d %H:%M:%S.%f"))
        self.assertEqual(2020, timestamp.year)
        self.assertEqual(12, timestamp.month)
        self.assertEqual(32, timestamp.day)

    def test_init_with_unsupported_values(self):
        with self.assertRaises(ValueError):
            timestamp = Endless2020DateTime(2020, 13, 1)

    @freeze_time("2021-01-02 00:00:00")
    def test_init_with_now(self):
        timestamp = Endless2020DateTime.now()
        self.assertEqual("2020-12-33 00:00:00.000000", timestamp.strftime("%Y-%m-%d %H:%M:%S.%f"))
        self.assertEqual(2020, timestamp.year)
        self.assertEqual(12, timestamp.month)
        self.assertEqual(33, timestamp.day)

    def test_strftime_day_of(self):
        timestamp = Endless2020DateTime(2020, 12, 31)
        self.assertEqual("2020-12-31 00:00:00.000000", timestamp.strftime("%Y-%m-%d %H:%M:%S.%f"))

    def test_strftime_dec_01_2020(self):
        timestamp = Endless2020DateTime(2005, 1, 1)
        self.assertEqual("2005-01-01 00:00:00.000000", timestamp.strftime("%Y-%m-%d %H:%M:%S.%f"))
        self.assertEqual("05-01- 1 00:00:00.000000", timestamp.strftime("%y-%m-%e %H:%M:%S.%f"))

    def test_strftime_day_after(self):
        timestamp = Endless2020DateTime(2021, 1, 1)
        self.assertEqual("2020-12-32 00:00:00.000000", timestamp.strftime("%Y-%m-%d %H:%M:%S.%f"))

    def test_strftime_nov_25_2022(self):
        timestamp = Endless2020DateTime(2022, 11, 25)
        self.assertEqual("2020-12-725 00:00:00.000000", timestamp.strftime("%Y-%m-%d %H:%M:%S.%f"))

    def test_strftime_nov_25_2022_iso_8601(self):
        timestamp = Endless2020DateTime(2022, 11, 25)
        self.assertEqual("2020-12-725T00:00:00", timestamp.isoformat())

    def test_strftime_nov_25_2022_human_friendly(self):
        timestamp = Endless2020DateTime(2022, 11, 25)
        self.assertEqual("Friday, December 725, 2020", timestamp.strftime("%A, %B %d, %Y"))

    def test_strftime_nov_01_2019_month_name_abbr(self):
        timestamp = Endless2020DateTime(2019, 11, 1)
        self.assertEqual("November Nov", timestamp.strftime("%B %b"))

    def test_strftime_nov_25_2022_rfc_822(self):
        timestamp = Endless2020DateTime(2022, 11, 25)
        self.assertEqual("Fri, 725 Dec 20 00:00:00 ", timestamp.strftime("%a, %d %b %y %H:%M:%S %z"))

    def test_strftime_nov_25_2022_localized_en_us(self):
        locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
        timestamp = Endless2020DateTime(2022, 11, 25)
        self.assertEqual("12/725/2020", timestamp.strftime("%x"))
        # self.assertEqual("Fri, 725 Dec 00:00:00 2020", timestamp.strftime("%c"))

    def test_strftime_pre_2020(self):
        timestamp = Endless2020DateTime(2019, 1, 1)
        self.assertEqual("2019-01-01 00:00:00.000000", timestamp.strftime("%Y-%m-%d %H:%M:%S.%f"))

    def test_strftime_week(self):
        sunday_before_new_year = Endless2020DateTime(2020, 12, 27)
        self.assertEqual("52", sunday_before_new_year.strftime("%U"))  # Sunday first
        self.assertEqual("51", sunday_before_new_year.strftime("%W"))  # Monday first
        self.assertEqual("52", sunday_before_new_year.strftime("%V"))  # ISO 8601 week number

        monday_before_new_year = Endless2020DateTime(2020, 12, 28)
        self.assertEqual("52", monday_before_new_year.strftime("%U"))  # Sunday first
        self.assertEqual("52", monday_before_new_year.strftime("%W"))  # Monday first
        self.assertEqual("53", monday_before_new_year.strftime("%V"))  # ISO 8601 week number

        sunday_after_new_year = Endless2020DateTime(2021, 1, 3)
        self.assertEqual("53", sunday_after_new_year.strftime("%U"))  # Sunday first
        self.assertEqual("52", sunday_after_new_year.strftime("%W"))  # Monday first
        self.assertEqual("52", sunday_after_new_year.strftime("%V"))  # ISO 8601 week number

        monday_after_new_year = Endless2020DateTime(2021, 1, 4)
        self.assertEqual("53", monday_after_new_year.strftime("%U"))  # Sunday first
        self.assertEqual("53", monday_after_new_year.strftime("%W"))  # Monday first
        self.assertEqual("53", monday_after_new_year.strftime("%V"))  # ISO 8601 week number
