# coding=utf-8
'''
Created on 2015年8月13日

@author: cooler
'''
import sys,os,time
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append(os.getcwd()+"/utils" )
from database import db_session

if __name__ == '__main__':
	mdb = db_session("beehoo")
	# userList = mdb.beehoo_user.find()
	# for user in userList:
	# 	user['user_id'] = user["userid"]
	# 	user['push_id'] = user["pushid"]
	# 	user['channel_id'] = ""
	# 	user['device_id'] = user["deviceid"]
	# 	user['device_type'] = user["devicetype"]
	# 	user['emergent_list'] = []
	# 	mdb.beehoo_user.save(user)
	for x in xrange(1,200):
		eventsList = mdb.events.find().limit(1000).skip(1000*x)
		for event  in eventsList:
			# print event
			# print event['crawled_date']
			try:
				event['crawled_date'] = time.mktime(time.strptime(event['crawled_date'],'%Y-%m-%d %H:%M:%S'))
				mdb.events.save(event)
			except Exception, e:
				# raise e
				pass
			# break
		print "----------------------------" + str(x)
		# break