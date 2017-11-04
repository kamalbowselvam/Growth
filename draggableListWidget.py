#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 21:24:50 2017

@author: bowman
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys, os


''' Creating a List Widget from where you can drag an item '''
class DragListWidget(QListWidget):
    def __init__(self, type, parent=None):
        super(DragListWidget, self).__init__(parent)
#        self.setIconSize(QSize(124, 124))

        self.setAcceptDrops(True)

    def mouseMoveEvent(self,event):    #Defining what happend when you try to move the item
        if event.buttons() == Qt.RightButton:
            data = QByteArray()             #Getting the QByteArray
            mime_data = QMimeData()         #Getting mimeData for the item 
            mime_data.setText(self.currentItem().text())   #Setting the current item Stock Symbol as a text to mime_data
            mime_text = "+Stock+"                  # A identifier that is used in plotterWidget to check if it is stockSymbol
            mime_data.setData(mime_text,data)      #Setting the mimedata 
            drag = QDrag(self)                      #Making it draggable
            drag.setMimeData(mime_data)
            drag.setHotSpot(self.rect().topLeft()) 
            print mime_text          
            dropAction = drag.start(Qt.MoveAction)   #Starting the drag option
