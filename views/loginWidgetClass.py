#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui


class LoginWidget(QtGui.QWidget):
    """LoginWidget"""

    def __init__(self):
        super(LoginWidget, self).__init__()
        self._main_layout = None
        self.initUI()

    def initUI(self):
        self._main_layout = QtGui.QVBoxLayout(self)
        form = QtGui.QFormLayout()
        username_line = QtGui.QLineEdit()
        form.addRow('Username', username_line)
        pwd_line = QtGui.QLineEdit()
        form.addRow('Password', pwd_line)
        self._main_layout.addLayout(form)
        submit = QtGui.QPushButton('Login')
        self._main_layout.addWidget(submit)
