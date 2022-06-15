import unittest
from src.src import *
import pandas as pd
import pandas.util.testing as pd_testing



class TestBMIFromData(unittest.TestCase):

    def testBMICategoryAndRisk(self):
        test_instance = BMIFromData()
        BMI1 = 14.37
        self.assertEqual(test_instance.BMICategoryAndRisk(BMI1), ("Underweight", "Malnutrition risk"))

        BMI2 = 100.
        self.assertEqual(test_instance.BMICategoryAndRisk(BMI2), ("Very severely obese", "Very high risk"))

        BMI3 = 24.91
        self.assertEqual(test_instance.BMICategoryAndRisk(BMI3), ("Normal weight", "Low risk"))

    def testEnrichDF(self):
        test_instance = BMIFromData(data=TESTDATAFILE)
        test_instance.showBMIinfo()

        reference_dict = { "Gender": ["Female", "Female"], "HeightCm": [166, 150], "WeightKg": [30, 100], "BMI": [10.9, 44.4], "BMI_category": ["Underweight", "Very severely obese"], "Health_risk": ["Malnutrition risk", "Very high risk"]}
        reference_df = pd.DataFrame.from_dict(reference_dict)

        pd_testing.assert_frame_equal(test_instance.json_df, reference_df)


if __name__ == '__main__':
    unittest.main()
