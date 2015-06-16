#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore
import requests
import json
import base64


class User(QtCore.QObject):
    """User class"""
    def __init__(self, username, password):
        super(User, self).__init__()
        self._username = username
        self._password = password
        self._logged = False

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    def login(self):
        headers = {
            'Content-Type': "application/json",
            'Authorization': self.auth
        }
        url = "http://localhost:8000/api/v1/employee/"
        response = requests.get(
            url,
            headers=headers
        )
        if response.status_code == 200:
            self._logged = True
            return True
        else:
            self._logged = False
            return False

    @property
    def auth(self):
        auth = self._username + ':' + self._password
        auth = base64.b64encode(auth)
        auth = 'Basic ' + auth
        return auth
