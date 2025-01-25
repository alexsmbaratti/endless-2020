import unittest
from datetime import datetime

from endless_2020.utils import get_day


class TestUtils(unittest.TestCase):

    def test_get_day(self):
        self.assertEqual(1, get_day(datetime(2019, 12, 1)))
        self.assertEqual(1, get_day(datetime(2020, 12, 1)))
        self.assertEqual(31, get_day(datetime(2020, 12, 31)))
        self.assertEqual(32, get_day(datetime(2021, 1, 1)))
