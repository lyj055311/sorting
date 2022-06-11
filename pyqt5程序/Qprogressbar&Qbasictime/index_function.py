# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from Ui_index import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.mythread={}
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        import Qthread
        self.mythread[1]=Qthread.MyThread(index=1)
        self.mythread[1].start()
        self.mythread[1].mysignal.connect(self.function)


    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        import Qthread
        self.mythread[2] = Qthread.MyThread(index=2)
        self.mythread[2].start()
        self.mythread[2].mysignal.connect(self.function)
    def function(self,cnt):
        index=self.sender().index
        if index==1:
            self.progressBar.setValue(cnt)
            self.lcdNumber.display(cnt)
        elif index==2:
            self.progressBar_2.setValue(cnt)
            self.lcdNumber_2.display(cnt)


