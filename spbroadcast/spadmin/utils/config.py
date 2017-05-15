#!/usr/bin/env python2.7
# coding=utf-8


import os
import ConfigParser

# CONF_PATH = os.path.abspath('..') + '/conf/pitaya.conf'
# print CONF_PATH


def initConfig():
    config = ConfigParser.RawConfigParser()
    config.read('./conf/spadmin.conf')
    return config
