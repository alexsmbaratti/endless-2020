import unittest
import main
from datetime import date


class TestCalculateDays(unittest.TestCase):

    def test_day_of(self):
        day_of = date(2020, 12, 31)
        self.assertEqual(0, main._calculate_date_delta(day_of))

    def test_day_after(self):
        day_of = date(2021, 1, 1)
        self.assertEqual(1, main._calculate_date_delta(day_of))

    def test_nov_25_2022(self):
        day_of = date(2022, 11, 25)
        self.assertEqual(694, main._calculate_date_delta(day_of))
