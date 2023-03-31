from sensor.constant.training_pipeline import SCHEMA_FILE_PATH
from sensor.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
from sensor.entity.config_entity import DataValidationConfig
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.utils.main_utils import read_yaml_file
import pandas as pd
import os,sys


class DataValidation:
   def __init__(self,data_ingestion_artifact:DataIngestionArtifact,data_validation_config:DataValidationConfig)
       try:
          self.data_ingestion_artifact=data_ingestion_artifact
          self.data_validation_config=data_validation_config
          self._schema_config =read_yaml_file(SCHEMA_FILE_PATH) 
       except Exception as e:
          raise SensorException(e,sys)
   
   def validate_number_of_columns(self,dataframe:pd.DataFrame)->bool:  
      try:
         number_of_columns=self._schema_config["columns"]
         if len(dataframe.columns)==number_of_columns:
           return True
         return False
      except Exception as e:
         raise SensorException(e,sys)
   def is_numerical_column_exist(self)->bool:
      pass
   @staticmethod
   def read_data(file_path)->pd.DataFrame:
      try:
         return pd.read_csv(file_path)
         
      except Exception as e:
        raise SensorException(e,sys)       
   def detect_dataset_drift(self):
      pass
   def initiate_data_validation(self)->DataValidationArtifact:
      try:
         train_file_path=self.data_ingestion_artifact.trained_file.path
         test_filea_path=self.data_ingestion_artifact.test_file.path   

         #reading data from train and test file location
         train_dataframe=DataValidation.read_data(train_file_path)
         test_dataframe=DataValidation.read_data(test_file_path)
         #validate number of columns

         status=self.validate_number_of_columns(dataframe=train_dataframe)
         if not status:
            error_message=f"{error_message}Train dataframe does not contain all columns."
         status = self.validate_number_of_column(dataframe=train_dataframe)       
      except Exception as e:   
         
         raise SensorException(e,sys)