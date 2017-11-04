#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 15:19:23 2017

@author: bowman
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 19:00:12 2017

@author: bowman
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from stocksDataRetriver import *
#from guiqwt.plot import CurveDialog, CurveWidget
#from guiqwt.builder import make  
import numpy as np
import matplotlib.pyplot as plt
import random

import sys


''' A Widget that could plot and get a Stock SYmbol when dropped '''
class plotWidget(QMainWindow):

    def __init__(self,parent):        
        super(plotWidget, self).__init__()
        # Just some button connected to `plot` method
        
        self.resize(200,200)
        
        but = QPushButton()
        but.setText('Create plot')
        self.connect(but,SIGNAL('clicked()'),self.plot)
        
        self.dcWidget = QDockWidget() 
        self.dcWidget.setFloating(True)
        
        
        self.dcWidget.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)
        self.AllowNestedDocks
        
        
        self.dcWidget2 = QDockWidget() 
        self.dcWidget2.setFloating(True)
        
                       
        
        self.dcWidget2.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)

        
        lay = QVBoxLayout()
        
        mainWidget = QWidget()        
        mainWidget.setLayout(lay)
        
        self.setCentralWidget(mainWidget)
    
    
    def dragEnterEvent(self, event):   # Defining the dragENterEvent 
            event.accept()
  
   
    def dragMoveEvent(self, event):    #Defning the DragMoveEvent
            event.accept()
            
            
    def dropEvent(self, event):     #Defininf the Drop Event 
        print "ghello"
        stockSymbol = event.mimeData().text()       #Getting MimeData Text, this text is set in DragableListWidget 
        if event.mimeData().hasFormat("+Stock+"):   #Checking if the dropped item is a stock 
            self.plot()                  #Plotting the StockSymbol

        else:
            print "hello"
            event.ignore()

#        return dockwidget    
        
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
        
        win = CurveDialog(edit=False, toolbar=True, parent=self)
        plot = win.get_plot()
        for item in items:
            plot.add_item(item)
#        win.show()
        self.addDockWidget(self.dcWidget)

        
        
    def dragEnterEvent(self, event):   # Defining the dragENterEvent 
            event.accept()
  
   
    def dragMoveEvent(self, event):    #Defning the DragMoveEvent
            event.accept()

        
    def dropEvent(self, event):     #Defininf the Drop Event 
        stockSymbol = event.mimeData().text()       #Getting MimeData Text, this text is set in DragableListWidget 
        if event.mimeData().hasFormat("+Stock+"):   #Checking if the dropped item is a stock 
            self.plot(stockSymbol)                  #Plotting the StockSymbol

        else:
            event.ignore()



class DockablePlotWidget(QDockWidget):
    LOCATION = Qt.RightDockWidgetArea
    def __init__(self, parent, plotwidgetclass, toolbar = None):
        super(DockablePlotWidget, self).__init__(parent)
        self.toolbar = toolbar
        layout = QHBoxLayout()
        self.plotwidget = plotwidgetclass()
        layout.addWidget(self.plotwidget)
        self.setLayout(layout)

    def get_plot(self):
        return self.plotwidget.plot




if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = plotWidget("AAPL")
    main.show()

    sys.exit(app.exec_())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
