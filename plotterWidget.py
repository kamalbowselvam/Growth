#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 19:00:12 2017

@author: bowman
"""
from guiqwt.plot import CurveDialog, CurveWidget
from guiqwt.builder import make 
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from stocksDataRetriver import * 
import numpy as np
import matplotlib.pyplot as plt
import random

import sys

''' A Widget that could plot and get a Stock SYmbol when dropped '''
class plotWidget(QWidget):

    def __init__(self,parent):        
        super(plotWidget, self).__init__()
        self.setAcceptDrops(True)
        # Just some button connected to `plot` method      
        self.resize(500,500)
        
        self.gWindow = CurveDialog(edit=False, toolbar=True)
        self.lay = QHBoxLayout()
        self.teditor = QLabel("Hello How are you")
        self.lay.addWidget(self.gWindow)
        self.setLayout(self.lay)
              
        
    def plot(self):
        ''' plot some random stuff '''
        x = np.linspace(0, 100, 1000)
       
        y = (np.random.rand(len(x))-0.5).cumsum()
    
        curve = make.curve(x, y, "ab", "b")
        range = make.range(0, 5)
        
        disp2 = make.computations(range, "TL",
                                  [(curve, "min=%.5f", lambda x,y: y.min()),
                                   (curve, "max=%.5f", lambda x,y: y.max()),
                                   (curve, "avg=%.5f", lambda x,y: y.mean())])
        legend = make.legend("TR")
        items = [ curve, range, disp2, legend]
        
        
        self.plotw = self.gWindow.get_plot()
        for item in items:
            self.plotw.add_item(item)
        
#        win.show()
        
    def dragEnterEvent(self, event):   # Defining the dragENterEvent 
            event.accept()
  
   
    def dragMoveEvent(self, event):    #Defning the DragMoveEvent
            event.accept()

        
    def dropEvent(self, event):     #Defininf the Drop Event 
#        stockSymbol = event.mimeData().text()       #Getting MimeData Text, this text is set in DragableListWidget
#        print stockSymbol
        if event.mimeData().hasFormat("+Stock+"):   #Checking if the dropped item is a stock 
            print "Hello"                  #Plotting the StockSymbol
            self.plot()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = plotWidget("APPL")
    main.show()

    sys.exit(app.exec_())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
