import os
import sys
import pandas as pd
from src.utils import load_object

from src.exception import CustomException
class PredictPipeline:
    def __init__(self) -> None:
        pass
    
    def predict(self,features):
        try:
            model_path=r'myenv\artifacts\model.pkl'
            preprocessor_path=r'myenv\artifacts\proprocessor.pkl'
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)
class CustomData:
    def __init__(self,
        Hour: int,
        Month: int,
        DayOfWeek: int,
        Vehicle_Type: int,
        FastagID: int,
        TollBoothID: int,
        Lane_Type: int,
        Vehicle_Dimensions: int,
        Transaction_Amount: float,
        Amount_paid: float,
        Geographical_Location: int,
        Vehicle_Speed: int):
        
        self.Hour = Hour

        self.Month = Month

        self.DayOfWeek = DayOfWeek

        self.Vehicle_Type = Vehicle_Type

        self.FastagID = FastagID

        self.TollBoothID = TollBoothID

        self.Lane_Type = Lane_Type

        self.Vehicle_Dimensions = Vehicle_Dimensions

        self.Transaction_Amount = Transaction_Amount

        self.Amount_paid = Amount_paid

        self.Geographical_Location = Geographical_Location

        self.Vehicle_Speed = Vehicle_Speed

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Hour": [self.Hour],
                "Month": [self.Month],
                "DayOfWeek": [self.DayOfWeek],
                "Vehicle_Type": [self.Vehicle_Type],
                "FastagID": [self.FastagID],
                "TollBoothID": [self.TollBoothID],
                "Lane_Type": [self.Lane_Type],
                "Vehicle_Dimensions": [self.Vehicle_Dimensions],
                "Transaction_Amount": [self.Transaction_Amount],
                "Amount_paid": [self.Amount_paid],
                "Geographical_Location": [self.Geographical_Location],
                "Vehicle_Speed": [self.Vehicle_Speed]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)