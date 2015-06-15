# -*- encoding: utf-8 -*-
import json
import os
import platform
import requests
import serial
import sys
import time

from dotenv import read_dotenv
from getenv import env

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

read_dotenv(os.path.join(BASE_DIR, '.env'))

API_USER = env('API_USER')
API_KEY = env('API_KEY')
API_URL = env('API_URL')


def logr(message):
    sys.stdout.flush()
    sys.stdout.write('\r%s' % message)


def logn(message):
    sys.stdout.flush()
    sys.stdout.write('\n%s' % message)


def logs(message):
    sys.stdout.write(' [%s]' % message)


def send(number):
    headers = {'content-type': 'application/json'}
    url = 'http://{}/api/v1/luggage/'.format(API_URL)
    params = {'username': API_USER, 'api_key': API_KEY}
    data = {'material_number': number}

    logs('Sending')
    response = requests.post(
        url,
        params=params,
        data=json.dumps(data),
        headers=headers
    )
    logs('Sent')
    logn('')
    response.raise_for_status()
