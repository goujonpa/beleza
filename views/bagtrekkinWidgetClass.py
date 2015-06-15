#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore


class BagtrekkinWidget(QtGui.QWidget):
    """BagtrekkinWidget"""

    def __init__(self, manager):
        super(BagtrekkinWidget, self).__init__()
        self._main_layout = QtGui.QVBoxLayout(self)
        self._manager = manager
        self._form = QtGui.QFormLayout()
        self._pnr = QtGui.QLineEdit()
        self._rfid = QtGui.QLineEdit()
        self._scan_button = QtGui.QPushButton('Scan Luggage')
        self._submit_button = QtGui.QPushButton('Send Luggage')
        self._form.addRow('PNR', self._pnr)
        self._form.addRow('RFID', self._rfid)
        self._main_layout.addLayout(self._form)
        self._main_layout.addWidget(self._scan_button)
        self._main_layout.addWidget(self._submit_button)
        self._scan_button.clicked.connect(self._scan)
        self._submit_button.clicked.connect(self._submit)

    @property
    def manager(self):
        return self._manager

    @QtCore.pyqtSlot()
    def _scan(self):
        pass

    @QtCore.pyqtSlot()
    def _submit(self):
        pass
