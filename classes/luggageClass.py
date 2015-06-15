#!/usr/bin/python
# -*- encoding: utf-8 -*-

import requests


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
        url = "http://localhost:8000/api/v1/checkin/"
        payload = "{\n  \"pnr\":\"TESTHJ\",\n  \"last_name\":\"goujon\",\n  \"material_number\":\"12345678\"\n}"
        headers = {
            'content-type': "application/json",
            'authorization': "ApiKey 39decbfab0fb1bae3f8136b153c2a401d543c4d3"
            }

        response = requests.request("POST", url, data=payload, headers=headers)
        response.raise_for_status()
