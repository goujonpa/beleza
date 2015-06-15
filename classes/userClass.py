#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore


class User(QtCore.QObject):
    """User class"""
    def __init__(self, login, password):
        super(User, self).__init__()
        self._login = login
        self._password = password

    @property
    def login(self):
        return self._login

    @property
    def password(self):
        return self._password
