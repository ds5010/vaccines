import unittest
import pandas as pd
from deaths import *

class DeathsTest(unittest.TestCase):
    def setUp():
        self.start = "05-01-2021.csv"
        self.end = "06-30-2021.csv"
        
    def test_get_death_number_JHU(self):
        # test case 01 from deaths.py
        df = get_death_number_JHU(self.start, self.end)
        # NEED TO ADD ASSERTS
    
    def test_get_confirm_number_JHU(self):
        df = get_confirm_number_JHU(self.start, self.end)
        # NEED TO ADD ASSERTS