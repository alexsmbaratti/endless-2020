import unittest
import main


class TestFormatDate(unittest.TestCase):

    def test_day_of(self):
        self.assertEqual("December 31, 2020", main.format_date(0))

    def test_day_after(self):
        self.assertEqual("December 32, 2020", main.format_date(1))

    def test_nov_25_2022(self):
        self.assertEqual("December 725, 2020", main.format_date(694))