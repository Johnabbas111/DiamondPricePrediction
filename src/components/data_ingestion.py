import os
import sys
import src.logger import logging
import src.exception import customException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
##iniatialize the data ingestion configration
@dataclass
class DataIngestionConfig:
    train_data_path=os.path.join('artifacts','tarin.csv')
    test_data_path=os.path.join('artifacts','test.csv')
    raw_data_path=os.path.join('artifacts','raw.csv')

##craeting a data ingestion class
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    def initiate_data_ingestion(self):
        logging.info("Data ingestion methods start")
        try:
            df=pd.read_csv(os.path.join('Notebook' 'gemstone.csv'))
            logging.info('Dataset read as pandas Dataframe')
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info('Train test split')
            train_set,test_set=train_test_split(df,test_size=0.30,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Ingestion of data is completed")
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )

        except Exception as e:
            logging.info('Error occured in data ingestion config ')