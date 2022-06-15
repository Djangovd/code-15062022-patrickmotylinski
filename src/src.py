import pandas as pd
import numpy as np

from env.paths import *
from env.vars import *

class BMIFromData:
    def __init__(self, data=DATAFILE):
        self.data = data
        self.json_df = pd.DataFrame()
        self.new_json_df = pd.DataFrame()

    def BMICategoryAndRisk(self, BMI):
        BMI = round(BMI,1)
        if BMI <= 18.4:
            return "Underweight", "Malnutrition risk"
        elif (BMI >= 18.5) and (BMI <= 24.9):
            return "Normal weight", "Low risk"
        elif (BMI >= 25.) and (BMI <= 29.9):
            return "Overweight", "Enhanced risk"
        elif (BMI >= 30.) and (BMI <= 34.9):
            return "Moderately obese", "Medium risk"
        elif (BMI >= 35.) and (BMI <= 39.9):
            return "Severely obese", "High risk"
        elif (BMI >= 40.):
            return "Very severely obese", "Very high risk"

    def json_to_pd(self):
        """
        Reads in JSON file with data, and creates a pandas dataframe of it
        :param data: JSON file containing weight data
        :return: pandas dataframe
        """
        self.json_df = pd.read_json(self.data)


    def enrich_df(self):
        """
        Enrich a dataframe feat. height and weight data with additional BMI columns
        :param df:
        :return:
        """

        self.json_df[df_cols.BMI.value] = round(self.json_df[df_cols.weight_kg.value] / pow(self.json_df[df_cols.height_cm.value]/100., 2), 1)

        self.json_df[df_cols.BMI_category.value] = self.json_df.apply(lambda x : self.BMICategoryAndRisk(x[df_cols.BMI.value])[0], 1)
        self.json_df[df_cols.Health_risk.value] = self.json_df.apply(lambda x : self.BMICategoryAndRisk(x[df_cols.BMI.value])[1], 1)

    def n_overweights(self, overweight_limit=25):
        return len(self.json_df.loc[self.json_df[df_cols.BMI.value] >= overweight_limit])

    def showBMIinfo(self):
        self.json_to_pd()
        self.enrich_df()
        print(self.json_df)
        print(f"Number of overweight individuals :  {self.n_overweights()}")
