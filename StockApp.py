#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 16:35:47 2017

@author: bowman
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore
from gettingStockDialog import *
from draggableListWidget import *
from plotterWidget import *
from plotterWidgetMat import *
import sys



class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow,self).__init__()
        
        self.setWindowTitle("Stocker")
        self.resize(800,500)
        
        self.mainWidget = QWidget()
        
        self.Vbox1 = QVBoxLayout()   # This will contain layers of the stocker app
        self.Hbox1 = QHBoxLayout()   # This will contain all the stocks and their plots  
        
        self.Vbox2 = QVBoxLayout()   # This will contauns stocks list and add remove buttons 
        
        self.addStockButton = QPushButton("Add")     #Button to call the getStock Dialog box
        self.removeStockButton = QPushButton("Remove")  #Button to remove the stock from List
        
        self.Hbox2 = QHBoxLayout()
        self.Hbox2.addWidget(self.addStockButton)
        self.Hbox2.addWidget(self.removeStockButton)      
        
        self.stocksList = DragListWidget(self)   # A draggable listwidget
        self.stocksList.addItem("AAPL")
        self.stocksList.addItem("GOOGL")
        self.stocksList.addItem("AMZN")
        self.stocksList.setFixedWidth(200)
        
        self.Vbox2.addWidget(self.stocksList)
        self.Vbox2.addLayout(self.Hbox2)
        
        self.stockDialog = getStockDialog(self.stocksList) #create a object from getStockDialog class
        self.addStockButton.clicked.connect(lambda: self.stockDialog.show()) #Calling the stock dialog
        self.removeStockButton.clicked.connect(lambda: self._removeStockfromList())    
        

        
        self.Hbox1.addLayout(self.Vbox2)
        self.Vbox1.addLayout(self.Hbox1)    
        
        self.pwidget = MatPlotWidget(self)      #A plotWidget that where you can drop the Stock Symbol
        self.Hbox1.addWidget(self.pwidget)   
        self.mainWidget.setLayout(self.Vbox1)
        self.setCentralWidget(self.mainWidget)
        
        
    def _removeStockfromList(self):     # FUnction to remove the stock from DragListWIdget 
       self.stocksList.takeItem(self.stocksList.currentRow())
      

def main():
    stock_simulation = QApplication(sys.argv)  
    stock_window = MainWindow()
    stock_window.show()
    stock_window.raise_()
    stock_simulation.exec_()
    


if __name__ == "__main__":
    main()    
    
