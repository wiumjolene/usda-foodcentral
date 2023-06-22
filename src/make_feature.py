import logging

import pandas as pd
import numpy as np
from src.utils import config
from src.utils.connect import DatabaseModelsClass
from src.get_data import GetData


class MakeFeatures:
    """ Class to make features of income statement. """
    logger = logging.getLogger(f"{__name__}.MakeFeatures")
    database_instance = DatabaseModelsClass('MYSQLLINUX')
    gt = GetData()

    def feature1(self):
        self.logger.info(f"Feature 1")
        df=self.gt.get_function()

        return df
