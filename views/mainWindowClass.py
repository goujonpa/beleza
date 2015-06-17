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
        self.setWindowTitle('Bagtrekkin - Checkin')
        self.loginView()
        self._process_stylesheet()
        self.showMaximized()

    @property
    def manager(self):
        return self._manager

    @QtCore.pyqtSlot()
    def loginView(self):
        self._central_widget = LoginWidget(self.manager)
        self.setCentralWidget(self._central_widget)
        self._central_widget.submit_signal.connect(self.bagtrekkinView)

    @QtCore.pyqtSlot()
    def bagtrekkinView(self):
        self._central_widget = BagtrekkinWidget(self.manager)
        self.setCentralWidget(self._central_widget)

    def _process_stylesheet(self):
        stylesheet = QtCore.QString("""
            QMainWindow
            {
                background-color: white;
            }
        """)
        self.setStyleSheet(stylesheet)
