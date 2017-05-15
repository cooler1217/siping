#encoding=utf-8
'''
测试输入
'''
from flask import Flask, request,make_response, render_template, redirect,url_for, session, abort, current_app
from flask_principal import Principal, Permission, UserNeed, RoleNeed, Identity, AnonymousIdentity, identity_changed, identity_loaded
from flup.server.fcgi import WSGIServer
from multiprocessing import Process
from werkzeug import secure_filename
import sys, logging, os, os.path
import math, time
import simplejson as json
from datetime import datetime, timedelta
from pymongo import ReplicaSetConnection, ReadPreference, Connection
from bson import ObjectId
from bson import json_util
import pymongo
import math,re
import traceback
import hashlib
import base64
import urllib2
from urllib import quote

from core import redisfactory

from core import calculator
from core.config import initConfig

# send email
import smtplib
from email.mime.text import MIMEText
from email.Header import Header
from email.MIMEMultipart import MIMEMultipart


LOG_FILENAME = './logs/test.log'
logging.basicConfig(filename=LOG_FILENAME, format='%(asctime)s - %(name)s - %(levelname)s - %(process)d - Line:%(lineno)d - %(message)s', level=logging.INFO)
logger = logging.getLogger('beehoo')
logger.setLevel(logging.DEBUG)

app = Flask(__name__)

@app.before_request
def before_request():
	real_ip = request.headers.get('X-Real-Ip', request.remote_addr)
	acc = request.headers.get('Accept')
	print real_ip
	print acc
	# typerequest.headers
	# print request.cookie

############## 头像上传
@app.route('/', methods=['GET', 'POST'])
def index():
	print type(request.headers)
	return "ddd"


if __name__ == '__main__':
    # main()
    # print "ddd"
    app.run(host='0.0.0.0',port=8090,debug=True)


# from interface import zsq

# if __name__ == '__main__':
# 	c = zsq.ConcreteComponet()
# 	c.operation()
# 	d1 = zsq.ConcreteDecoratorA()
# 	d1.setComponet(c)
# 	d1.operation()


