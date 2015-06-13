#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore


class LoginWidget(QtGui.QWidget):
    """LoginWidget"""
    _submit_signal = QtCore.pyqtSignal()

    def __init__(self, manager):
        super(LoginWidget, self).__init__()
        self._manager = manager
        self._main_layout = QtGui.QVBoxLayout(self)
        self._form = QtGui.QFormLayout()
        self._login = QtGui.QLineEdit()
        self._pwd = QtGui.QLineEdit()
        self._submit_button = QtGui.QPushButton('Login')
        self._form.addRow('Username', self._login)
        self._form.addRow('Password', self._pwd)
        self._pwd.setEchoMode(QtGui.QLineEdit.Password)
        self._main_layout.addLayout(self._form)
        self._main_layout.addWidget(self._submit_button)
        self.connect(
            self._submit_button,
            QtCore.SIGNAL('clicked()'),
            self._submit
        )

    @QtCore.pyqtSlot(str, str)
    def _submit(self):
        print(self._login.text())
        print(self._pwd.text())
        self._submit_signal.emit()
