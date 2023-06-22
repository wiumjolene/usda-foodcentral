# -*- coding: utf-8 -*-
import logging

from src.make_feature import MakeFeatures

class MainController:
    """ Decide which parts of the module to update. """
    logger = logging.getLogger(f"{__name__}.MainController")
    synch_data = False
    make_data = False
    feature = True

    def pipeline_control(self):

        if self.synch_data:
            self.logger.info('SYNC DATA')

        if self.make_data:
            self.logger.info('MAKE DATA')


        if self.feature:
            self.logger.info('--- FEATURE ---')
            mf = MakeFeatures()
            mf.feature1()
