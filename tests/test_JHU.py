import unittest
import os
import pandas as pd


class TestJHUData(unittest.TestCase):
    def setUp(self):
        self.files = ['deaths-05-01-2021-to-06-30-2021.csv',
                      'deaths-05-01-2021-to-05-31-2021.csv',
                      'deaths-05-01-2021-to-10-31-2021.csv',
                      'deaths-05-01-2021-to-09-30-2021.csv',
                      'deaths-05-01-2021-to-07-31-2021.csv',
                      'deaths-05-01-2021-to-08-31-2021.csv',
                      'deaths-05-01-2021-to-11-30-2021.csv']

    def test_files(self):
        """
        Checking for local CSVs with in directory data/JHU
        """
        list = os.listdir("data/JHU")
        self.assertEqual(self.files, list)

    def test_attributes(self):
        """
        Checking columns for "FIPS" and "Deaths"
        """
        for file in self.files:
            df = pd.read_csv("data/JHU/" + file)
            self.assertTrue("FIPS" in df.columns.values)
            self.assertTrue("Deaths" in df.columns.values)


if __name__ == '__main__':
    unittest.main()
