#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from classes.userClass import User


class LoginWidget(QtGui.QWidget):
    """LoginWidget"""
    submit_signal = QtCore.pyqtSignal()

    def __init__(self, manager):
        super(LoginWidget, self).__init__()
        self._manager = manager
        self._main_layout = QtGui.QVBoxLayout(self)
        self._form = QtGui.QFormLayout()
        self._username = QtGui.QLineEdit()
        self._pwd = QtGui.QLineEdit()
        self._submit_button = QtGui.QPushButton('Login')
        self._info = QtGui.QLabel()
        self._info.hide()
        self._form.addRow('Username', self._username)
        self._form.addRow('Password', self._pwd)
        self._pwd.setEchoMode(QtGui.QLineEdit.Password)
        self._main_layout.addLayout(self._form)
        self._main_layout.addWidget(self._submit_button)
        self._main_layout.addWidget(self._info)
        self._submit_button.clicked.connect(self._submit)

    @property
    def manager(self):
        return self._manager

    @property
    def username(self):
        return str(self._username.text())

    @property
    def pwd(self):
        return str(self._pwd.text())

    @QtCore.pyqtSlot()
    def _submit(self):
        self.manager._user = User(unicode(self.username), unicode(self.pwd))
        if self.manager._user.login():
            self._info.hide()
            self.submit_signal.emit()
        else:
            self._info.setText('Invalid username/password combination')
            self._info.show()
