import unittest

from endless_2020.endless_2020 import Endless2020DateTime


class TestEndless2020DateTime(unittest.TestCase):

    def test_strftime_day_of(self):
        timestamp = Endless2020DateTime(2020, 12, 31)
        self.assertEqual("2020-12-31 00:00:00.000000", timestamp.strftime("%Y-%m-%d %H:%M:%S.%f"))

    def test_strftime_day_after(self):
        timestamp = Endless2020DateTime(2021, 1, 1)
        self.assertEqual("2020-12-32 00:00:00.000000", timestamp.strftime("%Y-%m-%d %H:%M:%S.%f"))

    def test_strftime_nov_25_2022(self):
        timestamp = Endless2020DateTime(2022, 11, 25)
        self.assertEqual("2020-12-725 00:00:00.000000", timestamp.strftime("%Y-%m-%d %H:%M:%S.%f"))

    def test_strftime_nov_25_2022_human_friendly(self):
        timestamp = Endless2020DateTime(2022, 11, 25)
        self.assertEqual("Friday, December 725, 2020", timestamp.strftime("%A, %B %d, %Y"))

    def test_strftime_nov_25_2022_rfc_822(self):
        timestamp = Endless2020DateTime(2022, 11, 25)
        self.assertEqual("Fri, 725 Dec 20 00:00:00 ", timestamp.strftime("%a, %d %b %y %H:%M:%S %z"))

    def test_strftime_pre_2020(self):
        timestamp = Endless2020DateTime(2019, 1, 1)
        self.assertEqual("2019-01-01 00:00:00.000000", timestamp.strftime("%Y-%m-%d %H:%M:%S.%f"))
