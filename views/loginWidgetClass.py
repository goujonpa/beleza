#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from classes.userClass import User


class LoginWidget(QtGui.QWidget):
    """LoginWidget"""
    submit_signal = QtCore.pyqtSignal()

    def __init__(self, manager):
        super(LoginWidget, self).__init__()

        # Manager
        self._manager = manager

        # Main Layout
        self._layout = QtGui.QGridLayout()
        self.setLayout(self._layout)

        # Image
        self._img = QtGui.QPixmap('views/img/bt_logo.png')
        self._img = self._img.scaledToHeight(200, QtCore.Qt.SmoothTransformation)
        self._img_label = QtGui.QLabel()
        self._img_label.setPixmap(self._img)

        # Username
        self._username = QtGui.QLineEdit()
        self._username.setPlaceholderText('Username')

        # Password
        self._pwd = QtGui.QLineEdit()
        self._pwd.setPlaceholderText('Password')
        self._pwd.setEchoMode(QtGui.QLineEdit.Password)

        # Submit
        self._submit_button = QtGui.QPushButton('Login')

        # Info
        self._info = QtGui.QLabel()
        self._info.hide()

        # Spacer
        self._spacer_bottom = QtGui.QSpacerItem(500, 50, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)

        # Incorporation to main layout
        self._layout.addWidget(self._img_label, 1, 1, 1, 1, QtCore.Qt.AlignCenter)
        self._layout.addWidget(self._info, 2, 1, 1, 1, QtCore.Qt.AlignCenter)
        self._layout.addWidget(self._username, 3, 1, 1, 1, QtCore.Qt.AlignCenter)
        self._layout.addWidget(self._pwd, 4, 1, 1, 1, QtCore.Qt.AlignCenter)
        self._layout.addWidget(self._submit_button, 5, 1, 1, 1, QtCore.Qt.AlignCenter)
        self._layout.addItem(self._spacer_bottom, 6, 1, 1, 1)

        # Setting minimal row height
        self._layout.setRowMinimumHeight(0, 10)
        self._layout.setRowMinimumHeight(2, 20)
        self._layout.setRowMinimumHeight(5, 50)

        # SIGNALS SLOTS Connection
        self._submit_button.clicked.connect(self._submit)

        # STYLESHEET
        self._process_stylesheet()

        self.show()

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
                width: 200px;
                height: 30px;
                font-size: 14px;
                padding: 5px, 0px;
                padding-left: 5px;
            }
        """)
        self.setStyleSheet(stylesheet)
