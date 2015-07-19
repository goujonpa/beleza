#!/usr/bin/python
# -*- encoding: utf-8 -*-

import collections
import serial
import platform
import os
import requests
import time
import signal
import sys
import subprocess

PLATFORM_DARWIN = 'Darwin'
PLATFORM_LINUX = 'Linux'

BAUD_RATE = 9600

PORT_DARWIN = "/dev/tty.usbmodem1411"
PORT_LINUX = "/dev/ttyUSB0"

STEPS = ['-', '/', '|', '\\']


class Alarm(Exception):
    pass


def alarm_handler(signum, frame):
    raise Alarm


class TagReader(object):
    """class TagReader

    Attributes:
    port
    buf
    com

    """
    last_read = 0

    def __init__(self, *args, **kwargs):
        # self.port = self._getport()
        self.buf = collections.deque(maxlen=10)

    def __enter__(self):
        # try:
            # self.com = serial.Serial(self.port, baudrate=BAUD_RATE, timeout=1)
            # self.logn('Serial Com Connected\n')
        # except (serial.SerialException, OSError), e:
            # raise serial.SerialException(
                # 'Could not open serial port {}: {}'.format(self.port, e)
            # )
        return self

    def __exit__(self, type, value, traceback):
        pass
        # self.logn('Serial Com Disonnected\n')
        # if not self.com.closed:
            # self.com.close()

    def _readline(self):
        # return self.com.readline().strip()
        pwd = os.getcwd()
        signal.signal(signal.SIGALRM, alarm_handler)
        signal.alarm(60)  # 1 minutes
        try:
            sp = subprocess.Popen(
                [
                    'java',
                    '-classpath',
                    pwd + '/modules/java/bin:' + pwd + '/modules/java/lib/AlienRFID.jar',
                    'src.LeitorRfidCheckIn'
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            out, err = sp.communicate()
            signal.alarm(0)  # reset the alarm
        except Alarm:
            raise serial.SerialException('Java call is taking too long!')
        if out:
            if out[61:66] == "TAG: ":
                return out[66:-1]
            else:
                raise serial.SerialException('No TAG readen: ' + out)
        if err:
            raise serial.SerialException('Reading error: ' + err)

    # def _getport(self):
        # if platform.system() == PLATFORM_DARWIN:
            # return PORT_DARWIN
        # else:
            # return PORT_LINUX

    def readtag(self):
        try:
            if time.time() >= TagReader.last_read + 10:
                number = self._readline()
                if number and (number not in self.buf):
                    self.buf.append(number)
                    self.logr('Read %s' % number)
                    TagReader.last_read = time.time()
                    return number
            return None
        except serial.SerialException, e:
            raise serial.SerialException(
                'Could not readline from serial port'
            )

    def logr(self, message):
        sys.stdout.flush()
        sys.stdout.write('\r%s' % message)

    def logn(self, message):
        sys.stdout.flush()
        sys.stdout.write('\n%s' % message)

    def logs(self, message):
        sys.stdout.write(' [%s]' % message)
