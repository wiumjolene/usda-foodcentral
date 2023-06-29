import logging
import os
import pickle
import sys

import pandas as pd
from src.utils import config
from src.utils.connect import DatabaseModelsClass
from dotenv import find_dotenv, load_dotenv
import requests


class GetData:
    """ Class to etl data. """
    logger = logging.getLogger(f"{__name__}.GetIEData")
    #database_instance = DatabaseModelsClass('MYSQLLINUX')
    load_dotenv(find_dotenv())
    APIKEY = os.environ.get('USDAAPIKEY')

    def get_function(self):
        query_str = f""" 

        """
        df = self.database_instance.select_query(query_str=query_str)

        return df

    def get_food_list(self, datatype=None):
        if datatype==None:
            url = f""" https://api.nal.usda.gov/fdc/v1/foods/list?api_key={self.APIKEY}"""
        
        else:
            datatype = datatype.replace(" ", "%20")
            url = f""" https://api.nal.usda.gov/fdc/v1/foods/list?api_key={self.APIKEY}&dataType={datatype}"""

        response = requests.get(url)
        response=response.json()
        for _ in range(5):
            print(f"{response[_]['fdcId']} | {response[_]['description']} | {response[_]['dataType']} | {response[_]['publicationDate']}")
        
        return response
    

    def get_food_search(self, food_name):
        food = food_name.replace(" ", "%20")
        url = f""" https://api.nal.usda.gov/fdc/v1/foods/search?api_key={self.APIKEY}&query={food}"""
        response = requests.get(url)
        response=response.json()
        #df=pd.DataFrame(response)

        return response

    def get_food_fdcid(self, fdcId):
        url = f""" https://api.nal.usda.gov/fdc/v1/{fdcId}?api_key={self.APIKEY}"""
        response = requests.get(url)
        response=response.json()
        #df=pd.DataFrame(response)
        for _ in response:
            if isinstance(response[_], str):
                if _ in ['abstract', 'studyDesign', 'results']:
                    print(f"{_}: Scientific journal extract..")
                else:
                    print(f"{_}: {response[_]}")

            elif _ in ('ingredients'):
                print(f"{_}: LONG RESPONSE...")

            else:
                print(f"{_}: LONG RESPONSE...")

        return response
    

class GetGATSData:
    """ Class to etl data. """
    logger = logging.getLogger(f"{__name__}.GetGATSData")
    #database_instance = DatabaseModelsClass('MYSQLLINUX')
    load_dotenv(find_dotenv())
    APIKEY = os.environ.get('USDAAPI2KEY')
    DATA_FOLDER = os.path.join(config.ROOTDIR, 'data')

    def get_function(self):
        path = os.path.join(self.DATA_FOLDER, 'raw', 'import-customsdistricts-08081000apples.xlsx')
        df = pd.read_excel(path, engine='openpyxl')   

        df = df.melt(id_vars=['U.S. Custom Districts','Partner','Product','Year'],
                     var_name='Period', value_name='USD')

        return df

