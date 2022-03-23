import unittest
import os
import pandas as pd


class Testanimation(unittest.TestCase):
    def setUp(self):
        self.files = ['05-31-2021.png',
                      '06-30-2021.png',
                      '07-31-2021.png',
                      '08-31-2021.png',
                      '09-30-2021.png',
                      '10-31-2021.png',
                      '11-30-2021.png',
                      'animation.gif']

    def test_files(self):
        """
        Checking for local PNGs in directory img
        """
        list = os.listdir("../img")
        self.assertEqual(self.files, sorted(list))

if __name__ == '__main__':
    unittest.main()
