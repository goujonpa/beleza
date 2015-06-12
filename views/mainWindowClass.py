#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui


class MainWindow(QtGui.QMainWindow):
    """MainWindowClass"""

    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Bagtrekkin - Checkin')
        self.showMaximized()

    def loginView(self):
        pass
