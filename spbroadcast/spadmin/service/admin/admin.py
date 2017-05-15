#!/usr/bin/env python2.7
# coding=utf-8
"""
Created on 2014-12-9

@author: cooler
"""
import hashlib
import logging
import math
import re,os,shutil
import time
from datetime import datetime
from werkzeug import secure_filename

import pymongo
import simplejson as json
from bson import json_util
from bson import ObjectId
from flask import Blueprint, render_template, redirect, make_response, request,abort, g
from flask_principal import Permission, RoleNeed

from utils.database import initConnection
from conf import CONSTANT

admin = Blueprint('admin', __name__)

# Create a permission with a single Need, in this case a RoleNeed.
all_permission = Permission(RoleNeed('admin'), RoleNeed('operator'))
admin_permission = Permission(RoleNeed('admin'))

logger = logging.getLogger('admin')
logger.setLevel(logging.DEBUG)


@admin.before_request
def before_request():
    g.args = request.args if request.method == 'GET' else request.form
    logger.debug(request.path + "\t" + str(g.args))


@admin.teardown_request
def teardown_request(exception):
    # g.session.close()
    pass


@admin.route('page_not_found', methods=['GET'])
def page_not_found(error):
    return render_template('404.html')


@admin.route('/manager', methods=['GET'])
@all_permission.require(http_exception=401)
def manager():
    result = {"name": g.args.get("name", "noname")}
    response = make_response(json.dumps(result, default=json_util.default))
    response.headers['contents-type'] = 'application/json'
    return response


@admin.route('/', methods=['GET'])
@admin.route("/news_list/", methods=['POST', 'GET'])
@admin.route("/news_list/<num>", methods=['POST', 'GET'])
@all_permission.require(http_exception=401)
def index(num=0):
    title = request.args.get("title",'')
    author = request.args.get("author",'')
    ntype = request.args.get("ntype",'')
    status = request.args.get("status",'')
    numskip = int(num) * 10
    sql_news = "select * from spnews where status >-1 "
    sql_news_total = "select count(*)  from spnews where status >-1 "
    if status !='':
        sql_news += " and status="+status
        sql_news_total += " and status="+status
    if ntype !='':
        sql_news += " and ntype="+ntype
        sql_news_total += " and ntype="+ntype
    if title !='':
        sql_news += " and title like '%"+title+"%' "
        sql_news_total += " and title like '%"+title+"%' "
    if author !='':
        sql_news += " and author like '%"+author+"%' "
        sql_news_total += " and author like '%"+author+"%' "
    sql_news += " order by id desc limit "+str(numskip)+",10;"
    sql_news_total += ";"
    # sql_news = "select * from spnews where status >-1  and title like '%"+title+"%' and author like '%"+author+"%' and ntype ="+ntype+"and status = "+status+" order by id desc limit 10;"
    # print sql_news
    con = initConnection()
    cur = con.cursor()

    cur.execute(sql_news_total)
    total =int(math.ceil(cur.fetchone()[0]/10))
    cur.execute(sql_news)
    newsdatas = cur.fetchall()
    datas = []
    # print total,newsdatas
    for data in newsdatas:
        try:
            datas.append({
                    'id':data[0],
                    'title':data[1],
                    'shot_content':data[2],
                    'content':data[3],
                    'createtime':data[4],
                    'lastmodify':data[5],
                    'read_num':data[6],
                    'zan_num':data[7],
                    'author':data[8],
                    'src':data[9],
                    'reporter':data[10],
                    'desc':data[11],
                    'image_media_path':data[12],
                    'media_path':data[13],
                    'ntype':data[14],
                    'status':data[15],
                    'tags':data[16],
                    'zebian':data[17],#责任编辑
                })
        except Exception, e:
            raise e
            # pass
            # print data

    sql_spgroup = "select * from spgroup where status=1 order by id asc ;"
    con = initConnection()
    cur = con.cursor()

    cur.execute(sql_spgroup)
    fengmiandatas = cur.fetchall()
    sgdatas =[]
    for data in fengmiandatas:
        sgdatas.append({
            "id":data[0],
            "name":data[1],
            "createtime":data[2],
            "image_path":data[3],
            "status":data[4],
            "desc":data[5],
            })

    return render_template('news_list.html',
                           datas=datas,
                           sgdatas=sgdatas,
                           total=total,
                           title=title,
                           author=author,
                           ntype=ntype,
                           status=status,
                           num=int(num)
                           )


@admin.route("/getuserdata", methods=['POST', 'GET'])
@all_permission.require(http_exception=401)
def getuserdata():
    mdb = db_session('safego')
    u_total = mdb.beehoo_user.count()
    datestr = str(datetime.now())[0:10]
    dt = datetime(int(datestr[0:4]), int(datestr[5:7]), int(datestr[8:10]), 0, 0, 0)
    u_total_new = mdb.beehoo_user.find({'register_date': {'$gte': dt}}).count()
    datas = mdb.beehoo_login_history.find({'timestr': {'$gte': dt}})
    u_data = {}
    for data in datas:
        if u_data.has_key(data['userid']):
            u_data[data['userid']] = u_data[data['userid']] + 1
        else:
            u_data[data['userid']] = 1
    u_total_today_login = len(u_data)
    result = {
        "u_total": u_total,
        "u_total_new": u_total_new,
        "u_total_today_login": u_total_today_login
    }

    response = make_response(json.dumps({"result": result}, default=json_util.default))
    response.headers['content-type'] = 'application/json'
    return response



@admin.route("/addspnews/", methods=['POST', 'GET'])
@all_permission.require(http_exception=401)
def addspnews(num=0):
    sql_fengmian = "select * from fengmian order by id desc limit 10;"
    con = initConnection()
    cur = con.cursor()
    cur.execute(sql_fengmian)
    fengmiandatas = cur.fetchall()
    fdatas =[]
    for data in fengmiandatas:
        fdatas.append({
            "id":data[0],
            "title":data[1],
            "path":data[2],
            "status":data[3],
            "createtime":data[4],
            "lastmodify":data[5],
            "desc":data[6],
            })

    sql_shipin = "select * from shipin order by id desc ;"
    con = initConnection()
    cur = con.cursor()

    cur.execute(sql_shipin)
    fengmiandatas = cur.fetchall()
    sdatas =[]
    for data in fengmiandatas:
        sdatas.append({
            "id":data[0],
            "title":data[1],
            "path":data[2],
            "status":data[3],
            "createtime":data[4],
            "lastmodify":data[5],
            "desc":data[6],
            })

    sql_spgroup = "select * from spgroup where status=1 order by id asc ;"
    con = initConnection()
    cur = con.cursor()

    cur.execute(sql_spgroup)
    fengmiandatas = cur.fetchall()
    sgdatas =[]
    for data in fengmiandatas:
        sgdatas.append({
            "id":data[0],
            "name":data[1],
            "createtime":data[2],
            "image_path":data[3],
            "status":data[4],
            "desc":data[5],
            })

    sql_huodong = "select * from huodong where status=1 order by id desc;"
    con = initConnection()
    cur = con.cursor()

    cur.execute(sql_huodong)
    huodongdatas = cur.fetchall()
    hdatas =[]
    for data in huodongdatas:
        hdatas.append({
            "id":data[0],
            "name":data[1]
            })



    return render_template('addspnews.html',datas=[],fdatas=fdatas,sdatas=sdatas,sgdatas=sgdatas,hdatas=hdatas,)

@admin.route("/addfengmian/", methods=['POST', 'GET'])
@admin.route("/addfengmian/<num>", methods=['POST', 'GET'])
@all_permission.require(http_exception=401)
def addfengmian(num=0):
    title = request.args.get("title",'')
    status = request.args.get("status",'')
    numskip = int(num) * 10
    sql_fengmian = "select * from fengmian where 1=1"
    sql_fengmian_total = "select count(*) from fengmian where 1=1"
    if status !='':
        sql_fengmian += " and status="+status
        sql_fengmian_total += " and status="+status
    if title !='':
        sql_fengmian += " and name like '%"+title+"%' "
        sql_fengmian_total += " and name like '%"+title+"%' "
    sql_fengmian += " order by id desc limit "+str(numskip)+",10;"
    sql_fengmian_total += ";"

    con = initConnection()
    cur = con.cursor()

    cur.execute(sql_fengmian_total)
    total = int(math.ceil(cur.fetchone()[0]/10))
    # total = 1
    cur.execute(sql_fengmian)
    fengmiandatas = cur.fetchall()
    numskip = int(num) * 30
    datas =[]
    for data in fengmiandatas:
        datas.append({
            "id":data[0],
            "title":data[1],
            "path":data[2],
            "status":data[3],
            "createtime":data[4],
            "lastmodify":data[5],
            "desc":data[6],
            })

    return render_template('addfengmian.html',datas=datas,total=total,title=title,status=status,num=int(num))

@admin.route("/addshipin/", methods=['POST', 'GET'])
@all_permission.require(http_exception=401)
def addshipin(num=0):
    title = request.args.get("title",'')
    status = request.args.get("status",'')
    numskip = int(num) * 10
    sql_shipin = "select * from shipin where 1=1 "
    sql_shipin_total = "select count(*) from shipin where 1=1 "
    if status !='':
        sql_shipin += " and status="+status
        sql_shipin_total += " and status="+status
    if title !='':
        sql_shipin += " and name like '%"+title+"%' "
        sql_shipin_total += " and name like '%"+title+"%' "
    sql_shipin += " order by id desc limit "+str(numskip)+",10;"
    sql_shipin_total += ";"
    con = initConnection()
    cur = con.cursor()

    cur.execute(sql_shipin_total)
    total = int(math.ceil(cur.fetchone()[0]/10))
    cur.execute(sql_shipin)
    fengmiandatas = cur.fetchall()
    numskip = int(num) * 30
    datas =[]
    for data in fengmiandatas:
        datas.append({
            "id":data[0],
            "title":data[1],
            "path":data[2],
            "status":data[3],
            "createtime":data[4],
            "lastmodify":data[5],
            "desc":data[6],
            })

    return render_template('addshipin.html',datas=datas,total=total,title=title,status=status,num=int(num))


@admin.route("/addbanner/", methods=['POST', 'GET'])
@admin.route("/addbanner/<num>", methods=['POST', 'GET'])
@all_permission.require(http_exception=401)
def addbanner(num=0):
    title = request.args.get("title",'')
    status = request.args.get("status",'')
    numskip = int(num) * 10
    sql_banner = "select * from banner where status >-1  "
    sql_banner_total = "select count(*) from banner where status >-1   "
    if status !='':
        sql_banner += " and status="+status
        sql_banner_total += " and status="+status
    if title !='':
        sql_banner += " and name like '%"+title+"%' "
        sql_banner_total += " and name like '%"+title+"%' "
    sql_banner += " order by id desc limit "+str(numskip)+",10;"
    sql_banner_total += ";"
    con = initConnection()
    cur = con.cursor()

    cur.execute(sql_banner_total)
    total =int(math.ceil(cur.fetchone()[0]/10))
    cur.execute(sql_banner)
    bannerdatas = cur.fetchall()
    numskip = int(num) * 30
    datas =[]
    for data in bannerdatas:
        datas.append({
            "id":data[0],
            "title":data[1],
            "desc":data[2],
            "createtime":data[3],
            "image_path":data[4],
            "uri":data[5],
            "status":data[6],
            })

    return render_template('addbanner.html',datas=datas,total=total,title=title,status=status,num=int(num))

@admin.route('/uploadfile/', methods=['GET', 'POST'])
@all_permission.require(http_exception=401)
def uploadfile():
        try:
                f = request.files['file']
                ftype =  g.args.get('ftype')
                title = g.args.get('title')
                desc = g.args.get('desc')
                if ftype == "1":
                    fname = 'fengmian_'+str(time.time())[:10]+"_"+secure_filename(f.filename) #获取一个安全的文件名，且仅仅支持ascii字符；
                    filename_tmp = os.path.join(CONSTANT.UPLOAD_FOLDER_FENGMIAN, fname)
                    f.save(filename_tmp)
                    shutil.copyfile(filename_tmp,"../static/media/fengmian/" + fname)
                    sql_addfengmian = "INSERT INTO `fengmian` (`title`, `path`, `status`,`createtime`, `lastmodify`,`desc`) VALUES ('%s', '%s', 0,'%s', '%s','%s');" %(title,fname,str(datetime.now())[:19],str(datetime.now())[:19],desc)
                    logger.info(sql_addfengmian) 
                    con = initConnection()
                    cur = con.cursor()
                    res = cur.execute(sql_addfengmian)
                    con.commit()
                    logger.info("insert res:"+str(res))
                    return redirect("/admin/addfengmian")
                if ftype == "2":
                    fname = 'shipin-'+str(time.time())[:10]+"-"+secure_filename(f.filename) #获取一个安全的文件名，且仅仅支持ascii字符；
                    filename_tmp = os.path.join(CONSTANT.UPLOAD_FOLDER_SHIPIN, fname)
                    f.save(filename_tmp)
                    shutil.copyfile(filename_tmp,"../static/media/shipin/" + fname)
                    sql_addshipin = "INSERT INTO `shipin` (`title`, `path`, `status`,`createtime`, `lastmodify`,`desc`) VALUES ('%s', '%s', 0,'%s', '%s','%s');" %(title,fname,str(datetime.now())[:19],str(datetime.now())[:19],desc)
                    logger.info(sql_addshipin) 
                    con = initConnection()
                    cur = con.cursor()
                    res = cur.execute(sql_addshipin)
                    con.commit()
                    logger.info("insert res:"+str(res))
                    return redirect("/admin/addshipin")
                if ftype == "3":
                    uri = g.args.get('uri')
                    fname = 'banner_'+str(time.time())[:10]+"_"+secure_filename(f.filename) #获取一个安全的文件名，且仅仅支持ascii字符；
                    filename_tmp = os.path.join(CONSTANT.UPLOAD_FOLDER_BANNER, fname)
                    f.save(filename_tmp)
                    shutil.copyfile(filename_tmp,"../static/media/banner/" + fname)
                    sql_addbanner = "INSERT INTO `banner` (`name`, `desc`,`createtime`, `image_path`,`uri`, `status`) VALUES ('%s', '%s', '%s', '%s','%s',0);" %(title,desc,str(datetime.now())[:19],fname,uri)
                    logger.info(sql_addbanner) 
                    con = initConnection()
                    cur = con.cursor()
                    res = cur.execute(sql_addbanner)
                    con.commit()
                    logger.info("insert res:"+str(res))
                    return redirect("/admin/addbanner")
                if ftype == "4":
                    name = g.args.get('name')
                    sex = g.args.get('sex')
                    department = g.args.get('department')
                    abstract = g.args.get('abstract')
                    fname = 'presenter_'+str(time.time())[:10]+"_"+secure_filename(f.filename) #获取一个安全的文件名，且仅仅支持ascii字符；
                    filename_tmp = os.path.join(CONSTANT.UPLOAD_FOLDER_PRESENTER, fname)
                    f.save(filename_tmp)
                    shutil.copyfile(filename_tmp,"../static/media/presenter/" + fname)
                    sql_addzhuchiren = "INSERT INTO `presenter` (`name`, `sex`,`department`,`createtime`,`lastmodify`, `head_image`,`abstract`,`title`, `read_num`,`zan_num`,`status`,`ntype`) VALUES ('%s', '%s', '%s', '%s','%s','%s','%s','%s',0,0,0,0);" %(name,sex,department,str(datetime.now())[:19],str(datetime.now())[:19],fname,abstract,title)
                    logger.info(sql_addzhuchiren) 
                    con = initConnection()
                    cur = con.cursor()
                    res = cur.execute(sql_addzhuchiren)
                    con.commit()
                    logger.info("insert res:"+str(res))
                    return redirect("/admin/addzhuchiren")
                if ftype == "5":
                    fname = 'logo_'+str(time.time())[:10]+"_"+secure_filename(f.filename) #获取一个安全的文件名，且仅仅支持ascii字符；
                    filename_tmp = os.path.join(CONSTANT.UPLOAD_FOLDER_LOGO, fname)
                    f.save(filename_tmp)
                    shutil.copyfile(filename_tmp,"../static/media/logo/" + fname)
                    sql_addlogo = "INSERT INTO `splogo` (`name`, `path`, `status`,`createtime`,`desc`) VALUES ('%s', '%s', 0,'%s', '%s');" %(title,fname,str(datetime.now())[:19],desc)
                    logger.info(sql_addlogo) 
                    con = initConnection()
                    cur = con.cursor()
                    res = cur.execute(sql_addlogo)
                    con.commit()
                    logger.info("insert res:"+str(res))
                    return redirect("/admin/addlogo")
                if ftype == "6":
                    uri = g.args.get('uri','')
                    gtype = g.args.get('gtype','0')
                    fname = 'gonggao_'+str(time.time())[:10]+"_"+secure_filename(f.filename) #获取一个安全的文件名，且仅仅支持ascii字符；
                    filename_tmp = os.path.join(CONSTANT.UPLOAD_FOLDER_GONGGAO, fname)
                    f.save(filename_tmp)
                    shutil.copyfile(filename_tmp,"../static/media/gonggao/" + fname)
                    sql_addbanner = "INSERT INTO `gonggao` (`title`, `content`,`author`,`createtime`, `image_path`,`url`,`gtype`, `status`) VALUES ('%s', '%s','%s', '%s', '%s','%s',%s,0);" %(title,desc,'cooler',str(datetime.now())[:19],fname,uri,gtype)
                    logger.info(sql_addbanner) 
                    con = initConnection()
                    cur = con.cursor()
                    res = cur.execute(sql_addbanner)
                    con.commit()
                    logger.info("insert res:"+str(res))
                    return redirect("/admin/addgonggao")
                if ftype == "7":
                    logger.info(str(g.args))
                    gtype = int(g.args.get('gtype',1))
                    fname = 'spgroup_'+str(time.time())[:10]+"_"+secure_filename(f.filename) #获取一个安全的文件名，且仅仅支持ascii字符；
                    filename_tmp = os.path.join(CONSTANT.UPLOAD_FOLDER_GONGGAO, fname)
                    f.save(filename_tmp)
                    shutil.copyfile(filename_tmp,"../static/media/gonggao/" + fname)
                    sql_addbanner = "INSERT INTO `spgroup` ( `name`,`createtime`, `image_path`, `status`,`desc`,`gtype`) VALUES ('%s', '%s','%s',0,'%s',%s);" %(title,str(datetime.now())[:19],fname,desc,gtype)
                    logger.info(sql_addbanner) 
                    con = initConnection()
                    cur = con.cursor()
                    res = cur.execute(sql_addbanner)
                    con.commit()
                    logger.info("insert res:"+str(res))
                    return redirect("/admin/addspgroup")


        except Exception,e:
            logger.info(" except " + str(e) )
            return abort(404)
        # return redirect("/admin/addfengmian")
        # response = make_response(json.dumps(results, default=json_util.default))
        # response.headers['content-type'] = 'application/json'
        # return response

@admin.route("/savenews/", methods=['POST', 'GET'])
@all_permission.require(http_exception=401)
def savenews():
    title = g.args.get('title')
    shot_content =  g.args.get('shot_content')
    author = g.args.get('author')
    reporter = g.args.get('reporter')
    zebian = g.args.get('zebian')
    tags = g.args.get('tags')
    src = "四平广播电视台"
    desc = g.args.get('desc')
    ntype = g.args.get('ntype')
    huodongid = int(g.args.get('huodongid'))
    image_media_path = g.args.get('image_media_path')
    media_path = g.args.get('media_path')
    content = g.args.get('content')
    sql_addnews = """
    INSERT INTO `spnews`
     (`title`, `shot_content`, `content`,`createtime`, `lastmodify`,
        `read_num`,`zan_num`,`author`,`src`,`reporter`,`desc`,
        `image_media_path`,`media_path`,`ntype`,`status`,`tags`,`zebian`,`huodongid`)
         VALUES
          ('%s', '%s', '%s', '%s', '%s', %s, %s,'%s', '%s','%s', '%s', '%s', '%s', '%s',%s, '%s', '%s',%s);"""  %(title,shot_content,content,str(datetime.now())[:19],str(datetime.now())[:19],1,1,author,src,reporter,desc,image_media_path,media_path,ntype,0,tags,zebian,huodongid)
    
    logger.info(sql_addnews) 
    con = initConnection()
    cur = con.cursor()
    res = cur.execute(sql_addnews)
    con.commit()
    logger.info("insert res:"+str(res))
    response = make_response(json.dumps({"result": 1}, default=json_util.default))
    response.headers['content-type'] = 'application/json'
    return response


@admin.route("/deletenews/", methods=['POST', 'GET'])
@all_permission.require(http_exception=401)
def deletenews():
    nid = int(g.args.get('nid','0'))
    sql = """
    UPDATE `spbroadcast`.`spnews` SET `status`='-1' WHERE `id`='%s';
    """  %(nid)
    
    logger.info(sql) 
    con = initConnection()
    cur = con.cursor()
    res = cur.execute(sql)
    con.commit()
    logger.info("insert res:"+str(res))
    response = make_response(json.dumps({"result": 1}, default=json_util.default))
    response.headers['content-type'] = 'application/json'
    return response

@admin.route("/fabunews/", methods=['POST', 'GET'])
@all_permission.require(http_exception=401)
def fabunews():
    nid = int(g.args.get('nid','0'))
    sql = """
    UPDATE `spbroadcast`.`spnews` SET `status`='1' WHERE `id`='%s';
    """  %(nid)
    
    logger.info(sql) 
    con = initConnection()
    cur = con.cursor()
    res = cur.execute(sql)
    con.commit()
    logger.info("insert res:"+str(res))
    response = make_response(json.dumps({"result": 1}, default=json_util.default))
    response.headers['content-type'] = 'application/json'
    return response

@admin.route("/xiaxiannews/", methods=['POST', 'GET'])
@all_permission.require(http_exception=401)
def xiaxiannews():
    nid = int(g.args.get('nid','0'))
    sql = """
    UPDATE `spbroadcast`.`spnews` SET `status`='2' WHERE `id`='%s';
    """  %(nid)
    
    logger.info(sql) 
    con = initConnection()
    cur = con.cursor()
    res = cur.execute(sql)
    con.commit()
    logger.info("insert res:"+str(res))
    response = make_response(json.dumps({"result": 1}, default=json_util.default))
    response.headers['content-type'] = 'application/json'
    return response

@admin.route("/changebanner/", methods=['POST', 'GET'])
@all_permission.require(http_exception=401)
def changebanner():
    nid = int(g.args.get('nid','0'))
    status = int(g.args.get('status','0'))
    sql = """
    UPDATE `spbroadcast`.`banner` SET `status`='%s' WHERE `id`='%s';
    """  %(status,nid)
    
    logger.info(sql) 
    con = initConnection()
    cur = con.cursor()
    res = cur.execute(sql)
    con.commit()
    logger.info("insert res:"+str(res))
    response = make_response(json.dumps({"result": 1}, default=json_util.default))
    response.headers['content-type'] = 'application/json'
    return response


@admin.route("/addzhuchiren/", methods=['POST', 'GET'])
@admin.route("/addzhuchiren/<num>", methods=['POST', 'GET'])
@all_permission.require(http_exception=401)
def addzhuchiren(num=0):
    name = request.args.get("name",'')
    status = request.args.get("status",'')
    numskip = int(num) * 10
    sql_zhuchiren = "select * from presenter where 1=1"
    sql_zhuchiren_total = "select count(*) from presenter where 1=1"
    if status !='':
        sql_zhuchiren += " and status="+status
        sql_zhuchiren_total += " and status="+status
    if name !='':
        sql_zhuchiren += " and name like '%"+name+"%' "
        sql_zhuchiren_total += " and name like '%"+name+"%' "
    sql_zhuchiren += " order by id desc limit "+str(numskip)+",10;"
    sql_zhuchiren_total += ";"

    con = initConnection()
    cur = con.cursor()

    cur.execute(sql_zhuchiren_total)
    total = int(math.ceil(cur.fetchone()[0]/10))
    # total = 1
    cur.execute(sql_zhuchiren)
    zhuchirendatas = cur.fetchall()
    numskip = int(num) * 30
    datas =[]
    for data in zhuchirendatas:
        datas.append({
            "id":data[0],
            "name":data[1],
            "birthday":data[2],
            "sex":data[3],
            "department":data[4],
            "createtime":data[5],
            "lastmodify":data[6],
            "head_image":data[7],
            "abstract":data[8],
            "title":data[9],
            "read_num":data[10],
            "zan_num":data[11],
            "status":data[12],
            "ntype":data[13],
            })

    return render_template('addzhuchiren.html',datas=datas,total=total,name=name,status=status,num=int(num))


@admin.route("/huodonglist/", methods=['POST', 'GET'])
@admin.route("/huodonglist/<num>", methods=['POST', 'GET'])
@all_permission.require(http_exception=401)
def huodonglist(num=0):
    name = request.args.get("name",'')
    status = request.args.get("status",'')
    numskip = int(num) * 10
    sql_huodong = "select * from huodong where 1=1 and status > -1"
    sql_huodong_total = "select count(*) from huodong where 1=1 and status > -1 "
    if status !='':
        sql_huodong += " and status="+status
        sql_huodong_total += " and status="+status
    if name !='':
        sql_huodong += " and name like '%"+name+"%' "
        sql_huodong_total += " and name like '%"+name+"%' "
    sql_huodong += " order by id desc limit "+str(numskip)+",10;"
    sql_huodong_total += ";"

    con = initConnection()
    cur = con.cursor()

    cur.execute(sql_huodong_total)
    total = int(math.ceil(cur.fetchone()[0]/10))
    # total = 1
    cur.execute(sql_huodong)
    huodongdatas = cur.fetchall()
    numskip = int(num) * 30
    datas =[]
    for data in huodongdatas:
        datas.append({
            "id":data[0],
            "name":data[1],
            "content":data[2],
            "starttime":data[3],
            "endtime":data[4],
            "status":data[5],
            "author":data[6],
            "createtime":data[7],
            "lastmodify":data[8],
            })

    return render_template('huodonglist.html',datas=datas,total=total,name=name,status=status,num=int(num))

@admin.route("/addhuodong/", methods=['POST', 'GET'])
@admin.route("/addhuodong/<num>", methods=['POST', 'GET'])
@all_permission.require(http_exception=401)
def addhuodong(num=0):
    return render_template("addhuodong.html")

@admin.route("/uploadwang", methods=['POST', 'GET'])
@all_permission.require(http_exception=401)
def uploadwang():
    logger.info(str(request.files))
    # for x in request.files:
    #     logger.info("1")
    # return "http://127.0.0.1/static/images/appicon/3GfPHB2xhUuW4Ze.png"
    f = request.files['wangEditorH5File']
    if f is None:
        result = r"error|未成功获取文件，上传失败"
        return result
    else:
        fname = "huodong_"+'_'+secure_filename(f.filename)  # 获取一个安全的文件名，且仅仅支持ascii字符；
        filename_tmp = os.path.join("../spadmin/static/media/uploadwang/", fname)
        logger.info(filename_tmp)
        f.save(filename_tmp)
        shutil.copyfile(filename_tmp,"../static/media/uploadwang/" + fname)
        imgUrl = "/static/media/uploadwang/" + fname
        return imgUrl

@admin.route("/savehuodong/", methods=['POST', 'GET'])
@all_permission.require(http_exception=401)
def savehuodong():
    name = g.args.get('name')
    author = g.args.get('author')
    starttime = g.args.get('starttime')
    endtime = g.args.get('endtime')
    content = g.args.get('content')
    f = request.files['file']
    fname = 'huodong_'+str(time.time())[:10]+"_"+secure_filename(f.filename) #获取一个安全的文件名，且仅仅支持ascii字符；
    filename_tmp = os.path.join(CONSTANT.UPLOAD_FOLDER_HUODONG, fname)
    f.save(filename_tmp)
    shutil.copyfile(filename_tmp,"../static/media/huodong/" + fname)
    # print starttime,endtime,name,author
    # print content
    sql_addhuodong = """
    INSERT INTO `huodong`
     (`name`, `content`, `starttime`,`endtime`, `status`,
        `author`,`createtime`,`lastmodify`,`file_path`)
         VALUES
          ('%s', '%s', '%s', '%s', %s, '%s', '%s','%s','%s');"""  %(name,content,starttime,endtime,0,author,str(datetime.now())[:19],str(datetime.now())[:19],fname)
    
    logger.info(sql_addhuodong) 
    con = initConnection()
    cur = con.cursor()
    res = cur.execute(sql_addhuodong)
    con.commit()
    logger.info("insert res:"+str(res))
    response = make_response(json.dumps({"result": 1}, default=json_util.default))
    response.headers['content-type'] = 'application/json'
    return response

@admin.route("/changehuodong/", methods=['POST', 'GET'])
@all_permission.require(http_exception=401)
def changehuodong():
    nid = int(g.args.get('nid','0'))
    status = int(g.args.get('status','0'))
    sql = """
    UPDATE `spbroadcast`.`huodong` SET `status`='%s' WHERE `id`='%s';
    """  %(status,nid)
    
    logger.info(sql) 
    con = initConnection()
    cur = con.cursor()
    res = cur.execute(sql)
    con.commit()
    logger.info("insert res:"+str(res))
    response = make_response(json.dumps({"result": 1}, default=json_util.default))
    response.headers['content-type'] = 'application/json'
    return response


@admin.route("/addlogo/", methods=['POST', 'GET'])
@admin.route("/addlogo/<num>", methods=['POST', 'GET'])
@all_permission.require(http_exception=401)
def addlogo(num=0):
    # title = request.args.get("title",'')
    # status = request.args.get("status",'')
    numskip = int(num) * 10
    sql_logo = "select * from splogo where 1=1"
    sql_logo_total = "select count(*) from splogo where 1=1"
    # if status !='':
    #     sql_fengmian += " and status="+status
    #     sql_fengmian_total += " and status="+status
    # if title !='':
    #     sql_fengmian += " and name like '%"+title+"%' "
    #     sql_fengmian_total += " and name like '%"+title+"%' "
    sql_logo += " order by id desc limit "+str(numskip)+",10;"
    sql_logo_total += ";"

    con = initConnection()
    cur = con.cursor()

    cur.execute(sql_logo_total)
    total = int(math.ceil(cur.fetchone()[0]/10))
    # total = 1
    cur.execute(sql_logo)
    logodatas = cur.fetchall()
    numskip = int(num) * 30
    datas =[]
    for data in logodatas:
        datas.append({
            "id":data[0],
            "name":data[1],
            "path":data[2],
            "status":data[3],
            "createtime":data[4],
            "desc":data[5],
            })

    return render_template('addlogo.html',datas=datas,total=total,num=int(num))


@admin.route("/changelogo/", methods=['POST', 'GET'])
@all_permission.require(http_exception=401)
def changelogo():
    nid = int(g.args.get('nid','0'))
    status = int(g.args.get('status','0'))
    con = initConnection()
    cur = con.cursor()
    if status == 2:
        sql = """
        UPDATE `spbroadcast`.`splogo` SET `status`='%s' WHERE `id`='%s';
        """  %(status,nid) 
        logger.info(sql) 
        res = cur.execute(sql)
        con.commit()
        logger.info("insert res:"+str(res))
        result = 1
    else:
        sql = "select count(*) from splogo where status=1;"
        cur.execute(sql)
        total = int(cur.fetchone()[0])
        if total == 1:
            result = 2
        else:
            sql = """
            UPDATE `spbroadcast`.`splogo` SET `status`='%s' WHERE `id`='%s';
            """  %(status,nid) 
            logger.info(sql) 
            res = cur.execute(sql)
            con.commit()
            logger.info("insert res:"+str(res))
            result = 1
    response = make_response(json.dumps({"result": result}, default=json_util.default))
    response.headers['content-type'] = 'application/json'
    return response


@admin.route("/addgonggao/", methods=['POST', 'GET'])
@admin.route("/addgonggao/<num>", methods=['POST', 'GET'])
@all_permission.require(http_exception=401)
def addgonggao(num=0):
    title = request.args.get("title",'')
    status = request.args.get("status",'')
    numskip = int(num) * 10
    sql_logo = "select * from gonggao where 1=1"
    sql_logo_total = "select count(*) from gonggao where 1=1"
    if status !='':
        sql_logo += " and status="+status
        sql_logo_total += " and status="+status
    if title !='':
        sql_logo += " and title like '%"+title+"%' "
        sql_logo_total += " and title like '%"+title+"%' "
    sql_logo += " order by id desc limit "+str(numskip)+",10;"
    sql_logo_total += ";"

    con = initConnection()
    cur = con.cursor()

    cur.execute(sql_logo_total)
    total = int(math.ceil(cur.fetchone()[0]/10))
    # total = 1
    cur.execute(sql_logo)
    logodatas = cur.fetchall()
    numskip = int(num) * 30
    datas =[]
    for data in logodatas:
        datas.append({
            "id":data[0],
            "title":data[1],
            "content":data[2],
            "author":data[3],
            "createtime":data[4],
            "image_path":data[5],
            "uri":data[6],
            "gtype":data[7],
            "status":data[8],
            })

    return render_template('addgonggao.html',datas=datas,total=total,num=int(num))

@admin.route("/changegonggao/", methods=['POST', 'GET'])
@all_permission.require(http_exception=401)
def changegonggao():
    nid = int(g.args.get('nid','0'))
    status = int(g.args.get('status','0'))
    sql = """
    UPDATE `spbroadcast`.`gonggao` SET `status`='%s' WHERE `id`='%s';
    """  %(status,nid)
    
    logger.info(sql) 
    con = initConnection()
    cur = con.cursor()
    res = cur.execute(sql)
    con.commit()
    logger.info("insert res:"+str(res))
    response = make_response(json.dumps({"result": 1}, default=json_util.default))
    response.headers['content-type'] = 'application/json'
    return response

@admin.route("/addspgroup/", methods=['POST', 'GET'])
@admin.route("/addspgroup/<num>", methods=['POST', 'GET'])
@all_permission.require(http_exception=401)
def addspgroup(num=0):
    title = request.args.get("title",'')
    status = request.args.get("status",'')
    numskip = int(num) * 10
    sql_logo = "select * from spgroup where 1=1"
    sql_logo_total = "select count(*) from spgroup where 1=1"
    if status !='':
        sql_logo += " and status="+status
        sql_logo_total += " and status="+status
    if title !='':
        sql_logo += " and name like '%"+title+"%' "
        sql_logo_total += " and name like '%"+title+"%' "
    sql_logo += " order by id desc limit "+str(numskip)+",10;"
    sql_logo_total += ";"

    con = initConnection()
    cur = con.cursor()

    cur.execute(sql_logo_total)
    total = int(math.ceil(cur.fetchone()[0]/10))
    # total = 1
    cur.execute(sql_logo)
    logodatas = cur.fetchall()
    numskip = int(num) * 30
    datas =[]
    for data in logodatas:
        datas.append({
            "id":data[0],
            "title":data[1],
            "createtime":data[2],
            "image_path":data[3],
            "status":data[4],
            "desc":data[5],
            })

    return render_template('addspgroup.html',datas=datas,total=total,num=int(num))

@admin.route("/changespgroup/", methods=['POST', 'GET'])
@all_permission.require(http_exception=401)
def changespgroup():
    nid = int(g.args.get('nid','0'))
    status = int(g.args.get('status','0'))
    sql = """
    UPDATE `spbroadcast`.`spgroup` SET `status`='%s' WHERE `id`='%s';
    """  %(status,nid)
    
    logger.info(sql) 
    con = initConnection()
    cur = con.cursor()
    res = cur.execute(sql)
    con.commit()
    logger.info("insert res:"+str(res))
    response = make_response(json.dumps({"result": 1}, default=json_util.default))
    response.headers['content-type'] = 'application/json'
    return response


@admin.route("/uploadfengmian/", methods=['POST', 'GET'])
@all_permission.require(http_exception=401)
def uploadfengmian():
    logger.info(str(request.files))
    f = request.files['file']
    if f == None:
        result = r"error|未成功获取文件，上传失败"
        response = make_response(json.dumps({"result": results}, default=json_util.default))
        response.headers['content-type'] = 'application/json'
        return response
    else:
        fname = 'fengmian_'+str(time.time())[:10]+"_"+secure_filename(f.filename) #获取一个安全的文件名，且仅仅支持ascii字符；
        filename_tmp = os.path.join(CONSTANT.UPLOAD_FOLDER_FENGMIAN, fname)
        f.save(filename_tmp)
        shutil.copyfile(filename_tmp,"../static/media/fengmian/" + fname)
        logger.info(filename_tmp)
        imgUrl = fname
        response = make_response(json.dumps({"result": imgUrl}, default=json_util.default))
        response.headers['content-type'] = 'application/json'
        return response

@admin.route("/uploadshipin/", methods=['POST', 'GET'])
@all_permission.require(http_exception=401)
def uploadshipin():
    logger.info(str(request.files))
    f = request.files['file']
    if f == None:
        result = r"error|未成功获取文件，上传失败"
        response = make_response(json.dumps({"result": results}, default=json_util.default))
        response.headers['content-type'] = 'application/json'
        return response
    else:
        fname = 'shipin-'+str(time.time())[:10]+"-"+secure_filename(f.filename) #获取一个安全的文件名，且仅仅支持ascii字符；
        filename_tmp = os.path.join(CONSTANT.UPLOAD_FOLDER_SHIPIN, fname)
        f.save(filename_tmp)
        shutil.copyfile(filename_tmp,"../static/media/shipin/" + fname)
        logger.info(filename_tmp)
        imgUrl = fname
        response = make_response(json.dumps({"result": imgUrl}, default=json_util.default))
        response.headers['content-type'] = 'application/json'
        return response


@admin.route("/getfilesize/", methods=['POST', 'GET'])
@all_permission.require(http_exception=401)
def getfilesize():
    file_path = g.args.get("file_path","")
    if file_path == "":
        result = 0
    else:
        result = 1
    response = make_response(json.dumps({"result": result}, default=json_util.default))
    response.headers['content-type'] = 'application/json'
    return response