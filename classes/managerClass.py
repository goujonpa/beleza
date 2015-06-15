#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore


class Manager(QtCore.QObject):
    """Manager class"""
    def __init__(self):
        super(Manager, self).__init__()
        self._user = None

    @property
    def user(self):
        return self._user
