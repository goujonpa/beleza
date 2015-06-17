#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore


def alter_border_color(widget, color):
    stylesheet = '*{ border: 2px solid ' + color + '; }'
    stylesheet = QtCore.QString(stylesheet)
    widget.setStyleSheet(stylesheet)
