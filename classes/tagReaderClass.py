#!/usr/bin/python
# -*- encoding: utf-8 -*-

import collections
import serial
import platform
import os
import modules.rfid_reader as reader
import requests
import time

PLATFORM_DARWIN = 'Darwin'
PLATFORM_LINUX = 'Linux'

BAUD_RATE = 9600

PORT_DARWIN = "/dev/tty.usbmodem1411"
PORT_LINUX = "/dev/ttyUSB0"

STEPS = ['-', '/', '|', '\\']


class TagReader(object):
    """class TagReader

    Attributes:
    port
    buf
    com

    """
    last_read = 0

    def __init__(self, *args, **kwargs):
        self.port = self._getport()
        self.buf = collections.deque(maxlen=10)

    def __enter__(self):
        try:
            self.com = serial.Serial(self.port, baudrate=BAUD_RATE, timeout=1)
            reader.logn('Serial Com Connected\n')
        except (serial.SerialException, OSError), e:
            raise serial.SerialException(
                'Could not open serial port {}: {}'.format(self.port, e)
            )
        return self

    def __exit__(self, type, value, traceback):
        reader.logn('Serial Com Disonnected\n')
        if not self.com.closed:
            self.com.close()

    def _readline(self):
        return self.com.readline().strip()

    def _getport(self):
        if platform.system() == PLATFORM_DARWIN:
            return PORT_DARWIN
        else:
            return PORT_LINUX

    def readtag(self):
        try:
            if time.time() >= TagReader.last_read + 10:
                number = self._readline()
                if number and (number not in self.buf):
                    self.buf.append(number)
                    reader.logr('Read %s' % number)
                    TagReader.last_read = time.time()
                    return number
            return None
        except serial.SerialException, e:
            raise serial.SerialException(
                'Could not readline from serial port {}: {}'.format(self.port, e)
            )


if __name__ == '__main__':  # Ex code. shall be removec at long term
    try:
        with TagReader() as tagreader:
            i = 0
            try:
                while True:
                    reader.logr('Reading %s' % STEPS[i % 4])
                    number = tagreader.readtag()
                    if number:
                        reader.send(number)
                    time.sleep(0.1)
                    i += 1
            except (serial.SerialException, requests.exceptions.RequestException), e:
                reader.logn(e)
    except KeyboardInterrupt:
        pass
