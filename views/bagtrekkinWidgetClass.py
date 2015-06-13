#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui


class BagtrekkinWidget(QtGui.QWidget):
    """BagtrekkinWidget"""

    def __init__(self, manager):
        super(BagtrekkinWidget, self).__init__()
        self._main_layout = None
        self._manager = manager
        self.initUI()

    def initUI(self):
        self._main_layout = QtGui.QVBoxLayout(self)
        form = QtGui.QFormLayout()
        pnr = QtGui.QLineEdit()
        form.addRow('PNR', pnr)
        rfid = QtGui.QLineEdit()
        form.addRow('RFID', rfid)
        self._main_layout.addLayout(form)
        submit = QtGui.QPushButton('Send Luggage')
        self._main_layout.addWidget(submit)
