# coding=utf-8
'''
Created on 2015年8月13日

@author: gf
'''
import sys,os,time
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append(os.getcwd()+"/utils" )
import json
import redis
import time
import redisfactory 
from database import db_session

# mdb = db_session()
# datas = mdb.itzemail.find({"status":True})
# for data in datas:
#     data['status'] = 2
#     mdb.itzemail.save(data)


# ------------------------------------------------------------------------------------------------------------------------------------------

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_PASSWD = 'Beehoo@$^80'

redis_conn = redis.Redis(host=REDIS_HOST, port=REDIS_PORT,password=REDIS_PASSWD, db=11)
data_sms = {
                 'user_id':'',
                 'mobile':'',
                 'content':'',
                 'stype':'',
                 'createtime':'',
                 'sync':'',
                 'callback':'',
                 'hash_verify':''
                 }

data_email = {
    'user_id':'',
    'email':'',
    'title':'',
    'content':'',
    'stype':'',
    'createtime':'',
    'sync':'',
    'callback':'',
    'hash_verify':''
}

while True:
    dsms = data_sms.copy()
    demail = data_email.copy()
    print "-------------------------------------------------------"
    dsms['user_id'] = str(random.randint(10000, 100000))
    dsms['mobile'] = "18511995224"
    dsms['content'] = "爱亲好，恭喜您获得50元优惠券，投资5000元可用，有效期为2014-12-30至2015-1-29，请注意查收！"
    dsms['stype'] = 'couponexpires'
    # data['mobile'] = random.choice(['139', '188', '185', '136', '158', '151']) + "".join(random.choice("0123456789") for i in range(8))
    # data['content'] = ''.join(random.choice('zyxwvutsrqponmlkjihgfedcba') for i in range(random.randint(1, 50)))
    # data['stype'] = ''.join(random.choice('zyxwvutsrqponmlkjihgfedcba') for i in range(random.randint(5, 10)))
    dsms['sync'] = random.choice('01')
    dsms['callback'] = ''.join(random.choice('zyxwvutsrqponmlkjihgfedcba') for i in range(random.randint(1, 50)))
    dsms['createtime'] = int(time.time())
    # rdb = redisfactory.getDB(11)
    rdb = redis_conn
    rdb.rpush('sms', json.dumps(dsms))
    print dsms
    print "-------------------------------------------------------"
    # demail['user_id'] = str(random.randint(10000, 100000))
    # demail['email'] ='zhoupeng@itouzi.com'
    # demail['title'] = '周鹏测试'
    # demail['content'] = 'zp test 测试'
    # demail['stype'] = 'test'
    # demail['sync'] = random.choice('01')
    # demail['callback'] = ''.join(random.choice('zyxwvutsrqponmlkjihgfedcba') for i in range(random.randint(1, 50)))
    # demail['createtime'] = int(time.time())
    # rdb = redisfactory.getDB(11)
    # rdb.rpush('email', json.dumps(demail))
    # time.sleep(1)
    break