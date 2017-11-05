#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pandas as pd
from pandas_datareader import data, wb
from guiqwt.plot import CurveDialog, CurveWidget
from guiqwt.builder import make 
import guidata

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
        return self.stockDataFrame
        
if __name__ == '__main__':
    _app = guidata.qapplication()
    main = stockDataCollector("AAPL")
    sro = main._getStockdata()
    x1 = sro.index
    x2 = x1.Date
    y1 = sro['Close'].values
    curve = make.curve(x1, y1, "ab", "b")
    gWindow = CurveDialog(edit=False, toolbar=False) 
    plotw = gWindow.get_plot()
    plotw.add_item(curve)
    gWindow.show()
    gWindow.exec_()
