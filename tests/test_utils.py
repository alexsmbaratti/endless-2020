import unittest
from endless_2020.utils import strftime
from datetime import datetime


class TestUtils(unittest.TestCase):

    def test_strftime_day_of(self):
        day_of = datetime(2020, 12, 31)
        self.assertEqual("2020-12-31 00:00:00.000000", strftime(day_of))

    def test_strftime_day_after(self):
        day_of = datetime(2021, 1, 1)
        self.assertEqual("2020-12-32 00:00:00.000000", strftime(day_of))

    def test_strftime_nov_25_2022(self):
        day_of = datetime(2022, 11, 25)
        self.assertEqual("2020-12-725 00:00:00.000000", strftime(day_of))

    def test_strftime_nov_25_2022_human_friendly(self):
        day_of = datetime(2022, 11, 25)
        self.assertEqual("Friday, December 725, 2020", strftime(day_of, "%A, %B %d, %Y"))

    def test_strftime_nov_25_2022_rfc_822(self):
        day_of = datetime(2022, 11, 25)
        self.assertEqual("Fri, 725 Dec 20 00:00:00 ", strftime(day_of, "%a, %d %b %y %H:%M:%S %z"))

    def test_strftime_pre_2020(self):
        day_of = datetime(2019, 1, 1)
        self.assertEqual("2019-01-01 00:00:00.000000", strftime(day_of))
