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
        # Manager
        self._manager = Manager()

        # Central Widget
        self._central_widget = None
        self._loginView()

        # Menubar
        self._menubar = self.menuBar()
        self._user_menu = self._menubar.addMenu('User')
        self._logout_action = QtGui.QAction('Logout', self)
        self._user_menu.addAction(self._logout_action)

        # Window Title
        self.setWindowTitle('Bagtrekkin - Checkin')

        # SIGNALS SLOTS CONNECTIONS
        QtCore.QObject.connect(
            self._logout_action,
            QtCore.SIGNAL('triggered()'),
            self._logout
        )

        # STYLESHEET
        self._process_stylesheet()

        self.show()

    @property
    def manager(self):
        return self._manager

    @QtCore.pyqtSlot()
    def _loginView(self):
        self._central_widget = LoginWidget(self.manager)
        self.setCentralWidget(self._central_widget)
        QtCore.QObject.connect(
            self._central_widget,
            QtCore.SIGNAL('submit_signal()'),
            self._bagtrekkinView
        )

    @QtCore.pyqtSlot()
    def _bagtrekkinView(self):
        self._central_widget = BagtrekkinWidget(self.manager)
        self.setCentralWidget(self._central_widget)

    @QtCore.pyqtSlot()
    def _logout(self):
        self._manager._user = None
        self._loginView()

    def _process_stylesheet(self):
        stylesheet = QtCore.QString("""
            QMainWindow
            {
                background-color: white;
            }
        """)
        self.setStyleSheet(stylesheet)
