#!/usr/bin/python
# -*- encoding: utf-8 -*-

from classes.tagReaderClass import TagReader


def read():
    try:
        with TagReader() as tag_reader:
            i = 0
            try:
                while True:
                    tag_reader.logr('Reading %s' % STEPS[i % 4])
                    number = tag_reader.readtag()
                    if number:
                        return number
                    time.sleep(0.1)
                    i += 1
            except (
                serial.SerialException,
                requests.exceptions.RequestException
            ), e:
                tagreader.logn(e)
    except KeyboardInterrupt:
        pass
