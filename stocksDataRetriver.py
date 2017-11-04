#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 12:24:30 2017

@author: bowman
"""

import pandas as pd
from pandas_datareader import data, wb

import datetime 




class stockDataCollector(object):
    
    def __init__(self,stockName):
        super(stockDataCollector,self).__init__()
        self.stockName = stockName
        self.stockDataFrame = 0
        self.start = datetime.datetime(1900,1,1)
        self.end = datetime.date.today()
        

    def _getStockdata(self):
        self.stockDataFrame = data.DataReader(self.stockName,'yahoo',self.start,self.end)
        
        
#        
#start = datetime.datetime(2010,1,1)
#end = datetime.date.today()
#
#apple = data.DataReader('AAPL','yahoo',start,end)
#
#type(apple)
#
#import matplotlib.pyplot as plt 
#
#apple["Volume"].plot(grid = True)