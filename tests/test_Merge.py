import unittest
import os
import pandas as pd


class TestMergeData(unittest.TestCase):
    def setUp(self):
        self.files = ['vaccinations-and-deaths-07-31-2021.csv',
                      'vaccinations-and-deaths-08-31-2021.csv',
                      'vaccinations-and-deaths-11-30-2021.csv',
                      'vaccinations-and-deaths-06-30-2021.csv',
                      'vaccinations-and-deaths-10-31-2021.csv',
                      'vaccinations-and-deaths-05-31-2021.csv',
                      'vaccinations-and-deaths-09-30-2021.csv']

    def test_files(self):
        """
        Checking for local CSVs with in directory data/Merge 
        """
        list = os.listdir("data/Merge")
        self.assertEqual(self.files, list)

    def test_attributes(self):
        """
        Checking columns for "FIPS" ,"Recip_County","Recip_State","Series_Complete_18PlusPop_Pct" ,"Census2019_18PlusPop"and "Deaths"
        """
        for file in self.files:
            df = pd.read_csv("data/Merge/" + file)
            self.assertTrue("FIPS" in df.columns.values)
            self.assertTrue("Recip_County" in df.columns.values)
            self.assertTrue("Recip_State" in df.columns.values)
            self.assertTrue(
                "Series_Complete_18PlusPop_Pct" in df.columns.values)
            self.assertTrue("Census2019_18PlusPop" in df.columns.values)
            self.assertTrue("Deaths" in df.columns.values)


if __name__ == '__main__':
    unittest.main()
