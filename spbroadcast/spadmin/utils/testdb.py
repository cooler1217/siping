#!/usr/bin/env python2.7
# coding=utf-8
"""
Created on 2014-4-24

@author: cooler
"""
# pymongo 3.0
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from config import initConfig
import MySQLdb


def initConnection():
    config = initConfig()
    host = 'localhost'
    user = 'huicui360'
    pwd = 'C66a425bb92$^*#@339EF2C'
    db = 'spgd'
    con = MySQLdb.connect(host = host,user = user,passwd = pwd,db = db,charset = 'utf8')
    return con

if __name__ == '__main__':
    print "dddd"
    # for x in xrange(0,100000):
        # pass
    con = initConnection()
    print con
    sql_news = "show tables;"
    con = initConnection()
    cur = con.cursor()

    cur.execute(sql_news)
    newsdatas = cur.fetchall()
    print newsdatas
    con.close()
    print con
