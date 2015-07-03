#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from modules.arduino.read import read as arduino_read
from classes.luggageClass import Luggage
from modules.widgets.alter_color import alter_border_color
from requests.exceptions import RequestException


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
        QtCore.QObject.connect(
            self._scan_button,
            QtCore.SIGNAL('clicked()'),
            self._scan
        )
        QtCore.QObject.connect(
            self._submit_button,
            QtCore.SIGNAL('clicked()'),
            self._submit
        )

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
            self._info.setText(unicode('Scan error: Something went wrong, please try again.'))
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
        self._info.setText(unicode('Submitting Luggage...'))
        self._info.show()
        rfid = self.rfid
        pnr = self.pnr
        last_name = self.last_name
        luggage = Luggage(self.manager, rfid, pnr, last_name)
        try:
            luggage.send()

            # View
            alter_border_color(self._pnr, 'green')
            alter_border_color(self._last_name, 'green')
            self._info.setText(unicode('Success : Luggage submitted !'))

            # SIGNALS SLOTS CONNECTION
            QtCore.QObject.connect(
                self._pnr,
                QtCore.SIGNAL('textEdited(QString)'),
                self._reset_view
            )
            QtCore.QObject.connect(
                self._last_name,
                QtCore.SIGNAL('textEdited(QString)'),
                self._reset_view
            )
            QtCore.QObject.connect(
                self._rfid,
                QtCore.SIGNAL('textEdited(QString)'),
                self._reset_view
            )
        except RequestException:
            alter_border_color(self._pnr, 'red')
            alter_border_color(self._last_name, 'red')
            self._info.setText(unicode('Submit error: Something went wrong, please try again.'))
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

    @QtCore.pyqtSlot(str)
    def _reset_view(self):
        QtCore.QObject.disconnect(
            self._pnr,
            QtCore.SIGNAL('textEdited(QString)'),
            self._reset_view
        )
        QtCore.QObject.disconnect(
            self._last_name,
            QtCore.SIGNAL('textEdited(QString)'),
            self._reset_view
        )
        QtCore.QObject.disconnect(
            self._rfid,
            QtCore.SIGNAL('textEdited(QString)'),
            self._reset_view
        )
        self._info.hide()
        self._pnr.setStyleSheet('')
        self._last_name.setStyleSheet('')
        self._rfid.setStyleSheet('')
