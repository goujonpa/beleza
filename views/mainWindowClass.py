#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from views.loginWidgetClass import LoginWidget


class MainWindow(QtGui.QMainWindow):
    """MainWindowClass"""

    def __init__(self):
        super(MainWindow, self).__init__()
        self._central_widget = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Bagtrekkin - Checkin')
        self._central_widget = LoginWidget()
        self.setCentralWidget(self._central_widget)
        self.showMaximized()

    def loginView(self):
        pass
