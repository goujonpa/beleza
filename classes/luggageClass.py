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

    def send(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'ApiKey goujonpa:39decbfab0fb1bae3f8136b153c2a401d543c4d3'
            }
        url = "http://localhost:8000/api/v1/checkin/"
        data = {
            'pnr': 'YSVI82',
            'last_name': 'goujon',
            'material_number': 'E200 2996 9618 0246 2230 2CD7'
        }

        response = requests.post(
            url,
            data=json.dumps(data),
            headers=headers
        )
        response.raise_for_status()
