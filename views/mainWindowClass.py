#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from classes.managerClass import Manager
from views.loginWidgetClass import LoginWidget
from views.bagtrekkinWidgetClass import BagtrekkinWidget


class MainWindow(QtGui.QMainWindow):
    """MainWindowClass"""

    def __init__(self):
        super(MainWindow, self).__init__()
        self._central_widget = None
        self._manager = Manager()
        self._widgets = dict()
        self.initUI()

    @property
    def manager(self):
        return self._manager

    def initUI(self):
        self.setWindowTitle('Bagtrekkin - Checkin')
        self._widgets['login'] = LoginWidget(self.manager)
        self._widgets['login']._submit_signal.connect(self.bagtrekkinView)
        self._central_widget = self._widgets['login']
        self._widgets['bagtrekkin'] = BagtrekkinWidget(self.manager)
        self.setCentralWidget(self._widgets['login'])
        self.showMaximized()

    @QtCore.pyqtSlot()
    def loginView(self):
        self.setCentralWidget(self._widgets['login'])

    @QtCore.pyqtSlot()
    def bagtrekkinView(self):
        self.setCentralWidget(self._widgets['bagtrekkin'])
