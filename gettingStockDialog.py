#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 16:56:48 2017

@author: bowman
"""

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys, os

class Validator(QValidator):
    def validate(self,string,pos):
        return QValidator.Acceptable, string.upper(), pos 


class getStockDialog(QDialog):
    
    
    def __init__(self,stockList):
        super(getStockDialog,self).__init__()
        
        self.resize(500,200)
        
        self.stockName = 'Apple'
        self.stockSymbol = 'AAPL'
        self.stockList = stockList
        
        
        #Definition of two lineEdit and three button to get and clear stock Name and symbol
        
        self.verticalLayout = QVBoxLayout()
                
        self.stockNameLineEdit = QLineEdit()
        self.stockNameLabel = QLabel("Enter the Name of the Stock")       
        self.stockSymbolLineEdit = QLineEdit()
        self.stockSymbolLabel = QLabel("Enter the Symbol of the Stock")
        
        self.stockNameLineEdit.setText(self.stockName)
        self.stockSymbolLineEdit.setText(self.stockSymbol)
        
        self.addStockButton= QPushButton("Add")
        self.clearAllButton = QPushButton("Clear")
        self.closeDialogButton = QPushButton("Close")
        
        
        # Definition of a Validtor to make the Stock Symbol always Upper case
        
        self.validator = Validator(self)        
        self.stockSymbolLineEdit.setValidator(self.validator)
        
        
        self.verticalLayout.addWidget(self.stockNameLabel)
        self.verticalLayout.addWidget(self.stockNameLineEdit)
        
        self.verticalLayout.addWidget(self.stockSymbolLabel)
        self.verticalLayout.addWidget(self.stockSymbolLineEdit)
        
                
        self.HBox = QHBoxLayout()
        self.HBox.addWidget(self.addStockButton)
        self.HBox.addWidget(self.clearAllButton)
        self.HBox.addWidget(self.closeDialogButton)
        
        self.verticalLayout.addLayout(self.HBox)        
        self.setLayout(self.verticalLayout)
        
        
        #Calling the corresponding function 
        
        self.addStockButton.clicked.connect(lambda: self._addStockToList())
        self.clearAllButton.clicked.connect(lambda:  self._clearAll())
        self.closeDialogButton.clicked.connect(lambda: self.close())
        
        
        #Attribure to add the Stock Symbol to DragableListWidget

    def _addStockToList(self):
        self.stockName = self.stockNameLineEdit.text()
        self.stockSymbol = self.stockSymbolLineEdit.text()
        self.stockList.addItem(self.stockSymbol)

        #Atrribute To clear the Dialog line edits 

    def _clearAll(self):
        self.stockNameLineEdit.setText('')
        self.stockSymbolLineEdit.setText('')
                  
    
def main():
    getstock = QApplication(sys.argv)
    stock_window = getStockDialog()
    stock_window.show()
    stock_window.raise_()
    getstock.exec_()
    


if __name__ == "__main__":
    main()    