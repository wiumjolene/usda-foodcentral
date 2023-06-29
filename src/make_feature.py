import logging

import pandas as pd
import numpy as np
from src.utils import config
from src.utils.connect import DatabaseModelsClass
from src.get_data import GetGATSData


class MakeFeatures:
    """ Class to make features of income statement. """
    logger = logging.getLogger(f"{__name__}.MakeFeatures")
    gt = GetGATSData()

    def makeGraph(self):
        self.logger.info(f"makeGraph")
        df=self.gt.get_function()
        print(df)

        return df
