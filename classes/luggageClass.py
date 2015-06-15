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

    def send(self):
        url = "http://bagtrekkin.herokuapp.com/api/v1/checkin/"
        payload = "{\n  \"pnr\":\"X9JJB5\",\n  \"last_name\":\"rodde\",\n  \"material_number\":\"12345678\"\n}"
        headers = {
            'content-type': "application/json",
            'authorization': "ApiKey api730cd04e8f4c05e81459ed8efd6bb326deed7efb"
            }

        response = requests.request("POST", url, data=payload, headers=headers)
