#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from modules.arduino.read import read as arduino_read
from classes.luggageClass import Luggage
from modules.widgets.alter_color import alter_border_color


class BagtrekkinWidget(QtGui.QWidget):
    """BagtrekkinWidget"""

    def __init__(self, manager):
        super(BagtrekkinWidget, self).__init__()

        # Manager
        self._manager = manager

        # Main Layout
        self._layout = QtGui.QGridLayout(self)

        # PNR
        self._pnr = QtGui.QLineEdit()
        self._pnr.setPlaceholderText("Passenger's PNR")

        # Last name
        self._last_name = QtGui.QLineEdit()
        self._last_name.setPlaceholderText("Passenger's Last Name")

        # RFID
        self._rfid = QtGui.QLineEdit()
        self._rfid.setPlaceholderText("Luggage's RFID (autofill)")
        self._rfid.setReadOnly(True)

        # Scan
        self._scan_button = QtGui.QPushButton('Scan Luggage')

        # Submit
        self._submit_button = QtGui.QPushButton('Send Luggage')

        # Info
        self._info = QtGui.QLabel()
        self._info.hide()

        # Spacer
        self._spacer_bottom = QtGui.QSpacerItem(500, 50, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)

        # Incorporation to main layout
        self._layout.addWidget(self._info, 1, 1, 1, 1, QtCore.Qt.AlignCenter)
        self._layout.addWidget(self._pnr, 2, 1, 1, 1, QtCore.Qt.AlignCenter)
        self._layout.addWidget(self._last_name, 3, 1, 1, 1, QtCore.Qt.AlignCenter)
        self._layout.addWidget(self._rfid, 4, 1, 1, 1, QtCore.Qt.AlignCenter)
        self._layout.addWidget(self._scan_button, 5, 1, 1, 1, QtCore.Qt.AlignCenter)
        self._layout.addWidget(self._submit_button, 6, 1, 1, 1, QtCore.Qt.AlignCenter)
        self._layout.addItem(self._spacer_bottom, 7, 1, 1, 1)

        # Setting minimal row height
        self._layout.setRowMinimumHeight(0, 10)
        self._layout.setRowMinimumHeight(1, 20)
        self._layout.setRowMinimumHeight(5, 40)
        self._layout.setRowMinimumHeight(6, 40)

        # SIGNALS SLOTS  connection
        self._scan_button.clicked.connect(self._scan)
        self._submit_button.clicked.connect(self._submit)

        # STYLESHEET
        self._process_stylesheet()

        self.show()

    @property
    def manager(self):
        return self._manager

    @QtCore.pyqtSlot()
    def _scan(self):
        try:
            material_number = arduino_read()
            self._rfid.setText(unicode(material_number))
            alter_border_color(self._rfid, 'green')
            self._info.hide()
        except Exception:
            alter_border_color(self._rfid, 'red')
            self._info.setText('Scan error: Something went wrong, please try again.')
            self._info.show()

    @property
    def pnr(self):
        return unicode(self._pnr.text())

    @property
    def rfid(self):
        return unicode(self._rfid.text())

    @property
    def last_name(self):
        return unicode(self._last_name.text())

    @QtCore.pyqtSlot()
    def _submit(self):
        rfid = self.rfid
        pnr = self.pnr
        last_name = self.last_name
        luggage = Luggage(self.manager, rfid, pnr, last_name)
        try:
            luggage.send()
            alter_border_color(self._pnr, 'green')
            alter_border_color(self._last_name, 'green')
            self._info.hide()
            # add connect
        except Exception:
            alter_border_color(self._pnr, 'red')
            alter_border_color(self._last_name, 'red')
            self._info.setText('Submit error: Something went wrong, please try again.')
            self._info.show()

    def _process_stylesheet(self):
        stylesheet = QtCore.QString("""
            QPushButton
            {
                width: 200px;
                height: 30px;
                background-color: rgb(13, 173, 175);
                border: 1px solid white;
                color: white;
            }
            QLineEdit
            {
                width: 195px;
                height: 30px;
                font-size: 14px;
                padding: 5px, 0px;
                padding-left: 5px;
            }
        """)
        self.setStyleSheet(stylesheet)

    def reset_view(self):
        self._pnr.setStyleSheet('')
        self._last_name.setStyleSheet('')
        self._rfid.setStyleSheet('')
        self._info.hide()
