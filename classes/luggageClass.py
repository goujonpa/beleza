#!/usr/bin/python
# -*- encoding: utf-8 -*-

import requests
import json


class Luggage(object):
    """Luggage class"""

    def __init__(self, manager, material_number, pnr, last_name):
        super(Luggage, self).__init__()
        self._manager = manager
        self._material_number = material_number
        self._pnr = pnr
        self._last_name = last_name

    @property
    def manager(self):
        return self._manager

    @property
    def material_number(self):
        return self._material_number

    @property
    def pnr(self):
        return self._pnr

    @property
    def last_name(self):
        return self._last_name

    def send(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': self.manager._user.auth
            }
        url = "http://localhost:8000/api/v1/checkin/"
        data = {
            'pnr': self.pnr,
            'last_name': self.last_name,
            'material_number': self.material_number
        }

        response = requests.post(
            url,
            data=json.dumps(data),
            headers=headers
        )
        response.raise_for_status()
