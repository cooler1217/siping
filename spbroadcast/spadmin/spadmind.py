#!/usr/bin/env python2.7
# coding=utf-8
"""
Created on 2014-12-9

@author: cooler
"""
import hashlib
import logging
import logging.handlers
import os
import os.path
import traceback
from multiprocessing import Process

# 导入Flask
# from flup.server.fcgi import WSGIServer
from flask import request, render_template, redirect, session, current_app
from flask_principal import (Principal, UserNeed, RoleNeed, Identity, AnonymousIdentity,
                             identity_changed, identity_loaded)

from utils.database import initConnection
from utils.config import initConfig
# 导入message中的create_app
from service import create_app

# 初始化Flask放在message里面通过create_app创建
app = create_app()
app.config['MAX_CONTENT_LENGTH'] = 6000 * 1024 * 1024

logger = logging.getLogger()
logfile = logging.handlers.TimedRotatingFileHandler(os.path.join(os.getcwd(), './logs/' + "spadmin"), 'D', 1, 0)

# 设置后缀名称，跟strftime的格式一样
logfile.suffix = "%Y%m%d.log"
logger.addHandler(logfile)
formatter = logging.Formatter("%(asctime)s - %(name)s "
                              "- %(filename)s - %(funcName)s "
                              "- %(levelname)s - %(process)d "
                              "- Line:%(lineno)d - %(message)s")
logfile.setFormatter(formatter)
logger.setLevel(logging.DEBUG)


def isWhiteRouteList(path):
    whiteRouteList = [
        # "/user","/message","/safe/","/query","/money",
    ]
    for wl in whiteRouteList:
        if path.find(wl):
            return True
    return False


@app.before_request
def before_request():
    """Make sure we are connected to the database each request."""
    # 路径白名单
    whiteList = {'/': '根目录', '/auth': '登录验证', '/login': '登入', '/logout': '登出'}
    if str(request.path) in whiteList or isWhiteRouteList(request.path):
        pass
    else:
        if session.get("userinfo"):
            pass
        else:
            return redirect("/login")


@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    identity.user = session.get("userinfo")
    if session.get("userinfo"):
        identity.provides.add(UserNeed(session.get("userinfo")['account']))

        for role in session.get("userinfo")['roles']:
            identity.provides.add(RoleNeed(role))


@app.route("/auth", methods=['GET', 'POST'])
def auth():
    try:
        username = request.form.get('username').strip()
        password = request.form.get('password').strip()
        conn = initConnection()
        password_md5 = md5(password)
        sql_user = "select * from  "
        if username == "cooler" and password =="cooler1217":
            user = {
                "username":"cooler",
                "password":"59112f13bfa07e4a05312a30e35ba8ed",
                'priority':1,
                'group':'admin'
            }
        else:
            user = None
        # user = mdb.authority.find_one({"username": username, "password": password_md5})
        if user:
            user_info = dict()
            user_info['account'] = username
            if user['priority'] < 5:
                logger.info(str(user["priority"]))
                user_info['roles'] = ['admin']
            elif user['priority'] >= 16:
                logger.info("---------------------")
                user_info['roles'] = ['submitter']
            else:
                logger.info("---------------------")
                user_info['roles'] = ['operator']
            session["userinfo"] = user_info
            identity_changed.send(current_app._get_current_object(), identity=Identity(user_info['account']))
            logger.info("user login: account - %s, roles- %s" %
                        (session.get("userinfo").get("account"), session.get("userinfo").get("roles")))
            return redirect("/admin")
        else:
            return redirect("/login")
    except Exception, e:
        app.logger.error(traceback.format_exc(e))


def md5(str):
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()


@app.route('/', methods=['GET'])
@app.route('/login', methods=['GET'])
def login():
    return render_template("login.html")


@app.route("/logout", methods=['GET'])
def logout():
    if session.get('userinfo') is not None:
        app.logger.info("user logout: account - %s, roles- %s" % (
            session.get("userinfo").get("account"), session.get("userinfo").get("roles")))
        session.pop("userinfo")
        # Remove session keys set by Flask-Principal
        for key in ('identity.name', 'identity.auth_type'):
            session.pop(key, None)

        # Tell Flask-Principal the user is anonymous
        identity_changed.send(current_app._get_current_object(), identity=AnonymousIdentity())
    return redirect("/login")


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
# load the extension
principals = Principal(app)


def server(port):
    config = initConfig()
    host = config.get('server', 'host')
    WSGIServer(app, bindAddress=(host, port)).run()


def main():
    for x in xrange(1, 6):
        Process(target=server, args=(9010 + x,)).start()


if __name__ == '__main__':
    # main()
    app.run(host='0.0.0.0', port=9009, debug=True)
