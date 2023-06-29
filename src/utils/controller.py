# -*- coding: utf-8 -*-
import logging

from src.make_feature import MakeFeatures

class MainController:
    """ Decide which parts of the module to update. """
    logger = logging.getLogger(f"{__name__}.MainController")
    feature = True

    def pipeline_control(self):

        if self.feature:
            self.logger.info('--- FEATURE ---')
            mf = MakeFeatures()
            mf.makeGraph()
