#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from classes.tagReaderClass import TagReader


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
        try:
            with TagReader() as tagreader:
                i = 0
                try:
                    while True:
                        reader.logr('Reading %s' % STEPS[i % 4])
                        number = tagreader.readtag()
                        if number:
                            reader.send(number)
                        time.sleep(0.1)
                        i += 1
                except (serial.SerialException, requests.exceptions.RequestException), e:
                    reader.logn(e)
        except KeyboardInterrupt:
            pass


    @QtCore.pyqtSlot()
    def _submit(self):
        pass
