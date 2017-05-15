#-*- encoding: utf-8 -*-
from core.database import db_session
# import string, threading, time
# import urllib2
# from urllib import quote
# import json

# url = "http://api.map.baidu.com/geocoder?output=json&address="+quote("北京")
# # print url
# response = urllib2.urlopen(url) 
# html = response.read()

# print html

db =  db_session()
print db.push.find_one()