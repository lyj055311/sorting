# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot,QModelIndex
from PyQt5.QtWidgets import QMainWindow,QMessageBox,QHeaderView
from Ui_test import Ui_MainWindow
from model import Mod
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
        self.listView.setModel(Mod().mod1)
        self.tableView.setModel(Mod().mod_2)
        self.tableView.horizontalHeader().setStretchLastSection(True)#水平方向自适应
    @pyqtSlot(QModelIndex)
    def on_listView_clicked(self, index):
        """
        Slot documentation goes here.
        
        @param index DESCRIPTION
        @type QModelIndex
        """
        # TODO: not implemented yet
        qlist = ['按钮一', '按钮二', '按钮三', '按钮四']
        QMessageBox.information(self,'显示',str('点击的的是'+qlist[index.row()]))
        print("点击的是：" + str(index.row()))


