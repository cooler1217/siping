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
    host = config.get('database', 'host')
    user = config.get('database', 'user')
    pwd = config.get('database', 'pwd')
    db = config.get('database', 'db')
    con = MySQLdb.connect(host = host,user = user,passwd = pwd,db = db,charset = 'utf8')
    return con

if __name__ == '__main__':
    print "dddd"
    # for x in xrange(0,100000):
        # pass
    con = initConnection()
    print con
    sql_news = "select * from spnews where title like '%"+"dd"+"%' order by id desc limit 10;"
    sql_news_total = "select count(*) from spnews;"
    con = initConnection()
    cur = con.cursor()

    cur.execute(sql_news_total)
    total = cur.fetchone() 
    cur.execute(sql_news)
    newsdatas = cur.fetchall()
    datas = []
    print total
    print newsdatas
    con.close()
    print con
