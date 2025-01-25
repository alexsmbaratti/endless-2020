import locale
import unittest

from endless_2020.endless_2020 import Endless2020DateTime


class TestEndless2020DateTime(unittest.TestCase):

    def test_init_with_endless_format(self):
        timestamp = Endless2020DateTime(2020, 12, 32)
        self.assertEqual("2020-12-32 00:00:00.000000", timestamp.strftime("%Y-%m-%d %H:%M:%S.%f"))
        self.assertEqual(32, timestamp.day)

    def test_init_with_unsupported_values(self):
        with self.assertRaises(ValueError):
            timestamp = Endless2020DateTime(2020, 13, 1)

    def test_strftime_day_of(self):
        timestamp = Endless2020DateTime(2020, 12, 31)
        self.assertEqual("2020-12-31 00:00:00.000000", timestamp.strftime("%Y-%m-%d %H:%M:%S.%f"))

    def test_strftime_dec_01_2020(self):
        timestamp = Endless2020DateTime(2020, 12, 1)
        self.assertEqual("2020-12-01 00:00:00.000000", timestamp.strftime("%Y-%m-%d %H:%M:%S.%f"))
        self.assertEqual("2020-12- 1 00:00:00.000000", timestamp.strftime("%Y-%m-%e %H:%M:%S.%f"))

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
