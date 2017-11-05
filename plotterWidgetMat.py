#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 19:34:29 2017

@author: bowman
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from stocksDataRetriver import * 
import numpy as np
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import random

import sys

class ZoomPan:
    def __init__(self):
        self.press = None
        self.cur_xlim = None
        self.cur_ylim = None
        self.x0 = None
        self.y0 = None
        self.x1 = None
        self.y1 = None
        self.xpress = None
        self.ypress = None


    def zoom_factory(self, ax, base_scale = 2.):
        def zoom(event):
            cur_xlim = ax.get_xlim()
            cur_ylim = ax.get_ylim()

            xdata = event.xdata # get event x location
            ydata = event.ydata # get event y location

            if event.button == 'down':
                # deal with zoom in
                scale_factor = 1 / base_scale
            elif event.button == 'up':
                # deal with zoom out
                scale_factor = base_scale
            else:
                # deal with something that should never happen
                scale_factor = 1
                print event.button

            new_width = (cur_xlim[1] - cur_xlim[0]) * scale_factor
            new_height = (cur_ylim[1] - cur_ylim[0]) * scale_factor

            relx = (cur_xlim[1] - xdata)/(cur_xlim[1] - cur_xlim[0])
            rely = (cur_ylim[1] - ydata)/(cur_ylim[1] - cur_ylim[0])

            ax.set_xlim([xdata - new_width * (1-relx), xdata + new_width * (relx)])
            ax.set_ylim([ydata - new_height * (1-rely), ydata + new_height * (rely)])
            ax.figure.canvas.draw()

        fig = ax.get_figure() # get the figure of interest
        fig.canvas.mpl_connect('scroll_event', zoom)

        return zoom

    def pan_factory(self, ax):
        def onPress(event):
            if event.inaxes != ax: return
            self.cur_xlim = ax.get_xlim()
            self.cur_ylim = ax.get_ylim()
            self.press = self.x0, self.y0, event.xdata, event.ydata
            self.x0, self.y0, self.xpress, self.ypress = self.press

        def onRelease(event):
            self.press = None
            ax.figure.canvas.draw()

        def onMotion(event):
            if self.press is None: return
            if event.inaxes != ax: return
            dx = event.xdata - self.xpress
            dy = event.ydata - self.ypress
            self.cur_xlim -= dx
            self.cur_ylim -= dy
            ax.set_xlim(self.cur_xlim)
            ax.set_ylim(self.cur_ylim)

            ax.figure.canvas.draw()

        fig = ax.get_figure() # get the figure of interest

        # attach the call back
        fig.canvas.mpl_connect('button_press_event',onPress)
        fig.canvas.mpl_connect('button_release_event',onRelease)
        fig.canvas.mpl_connect('motion_notify_event',onMotion)

        #return the function
        return onMotion

''' A Widget that could plot and get a Stock SYmbol when dropped '''
class MatPlotWidget(QWidget):

    def __init__(self,parent):        
        super(MatPlotWidget, self).__init__()
        self.setAcceptDrops(True)
        # Just some button connected to `plot` method      
        self.resize(500,500)
        
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        

        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
              
        
    def plot(self,pdDataFrame):
        ''' plot some random stuff '''
        x1 = pdDataFrame.index
        y1 = pdDataFrame['Close']
        x = np.linspace(0, 100, 1000)
       
        y = (np.random.rand(len(x))-0.5).cumsum()
    
        ax = self.figure.add_subplot(111)
        ax.clear()
        ax.grid()
        ax.plot(x1,y1,'-o',  markersize=1, color='r')   
        zp = ZoomPan()
        scale = 1.1
        figZoom = zp.zoom_factory(ax, base_scale = scale)
        figPan = zp.pan_factory(ax)

        # refresh canvas
        self.canvas.draw()

    def dragEnterEvent(self, event):   # Defining the dragENterEvent 
            event.accept()
  
   
    def dragMoveEvent(self, event):    #Defning the DragMoveEvent
            event.accept()

        
    def dropEvent(self, event):     #Defininf the Drop Event 
        stockSymbol = event.mimeData().text()       #Getting MimeData Text, this text is set in DragableListWidget
        print stockSymbol
        if event.mimeData().hasFormat("+Stock+"):   #Checking if the dropped item is a stock 
                                    #Plotting the StockSymbol
            print stockSymbol
            stockData = stockDataCollector(stockSymbol)
            pdDataFrame = stockData._getStockdata()
            self.plot(pdDataFrame)
        else:
            event.ignore()
if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = MatPlotWidget()
    main.show()

    sys.exit(app.exec_())
        
                    
            