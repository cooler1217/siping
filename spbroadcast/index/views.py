#encoding=utf-8
'''
Created on 2015-7-1

@author: cooler
'''
import sys,os
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append(os.getcwd()+"/utils" )
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
import json
from datetime import datetime
import time
import hashlib
import base64
import urllib2
import logging
from .models import User
from .models import Group
from .models import Spnews
from .models import Banner
from .models import Huodong
from .models import Toupiaoyanzheng
from .models import Splogo
from .models import Gonggao
from .models import Spgroup


def getMd5Value(src):
    myMd5 = hashlib.md5()
    myMd5.update(src)
    myMd5_Digest = myMd5.hexdigest()
    return myMd5_Digest

# Create your views here.

def clientType(user_client):
	client_list = [
	      'nokia', 'sony', 'ericsson', 'mot', 'samsung', 'htc', 'sgh', 'lg', 'sharp', 'sie-'
	      ,'philips', 'panasonic', 'alcatel', 'lenovo', 'iphone', 'ipod', 'blackberry', 'meizu', 
	      'android', 'netfront', 'symbian', 'ucweb', 'windowsce', 'palm', 'operamini', 
	      'operamobi', 'opera mobi', 'openwave', 'nexusone', 'cldc', 'midp', 'wap', 'mobile'
	]
	for client in client_list:
		if user_client.find(client) > 0:
			return True
	return False
	

def cooler(request):
	return render(request, 'cooler.html',)

def index(request):
	logoList = Splogo.objects.filter(status=1).all()[:1]
	if logoList.count() == 0:
		logo_path = "/static/style/imgs/logo.png"
	else:
		for logo in logoList:
			logo_path = "/static/media/logo/"+logo.path
	userinfo = request.session.get("userinfo",default=None)
	banners = Banner.objects.filter(status=1).order_by('-id').all()[:4]
	spxw_list = Spnews.objects.filter(ntype=1,status=1).order_by('-id').all()[:4]
	znsb_list = Spnews.objects.filter(ntype=2,status=1).order_by('-id').all()[:4]
	qxxw_list = Spnews.objects.filter(ntype=3,status=1).order_by('-id').all()[:4]
	spzb_list = Spnews.objects.filter(ntype=4,status=1).order_by('-id').all()[:5]
	jplm_list = Spnews.objects.filter(ntype=5,status=1).order_by('-id').all()[:5]
	dtlm_list = Spnews.objects.filter(ntype=6,status=1).order_by('-id').all()[:5]
	gonggao_list = Gonggao.objects.filter(status=1).order_by('-id').all()[:6]
	spgroup_list = Spgroup.objects.filter(status=1).order_by('-id').all()[:1]
	results = {"userinfo":userinfo,"logo":logo_path,"gonggao_list":gonggao_list,"spgroup_list":spgroup_list,"banners":banners,"spxw_list":spxw_list,"znsb_list":znsb_list,"qxxw_list":qxxw_list,"jplm_list":jplm_list,"spzb_list":spzb_list,"dtlm_list":dtlm_list}
	return render(request, 'index.html',{"response":results})

def sipingxinwen(request):
	logoList = Splogo.objects.filter(status=1).all()[:1]
	if logoList.count() == 0:
		logo_path = "/static/style/imgs/logo.png"
	else:
		for logo in logoList:
			logo_path = "/static/media/logo/"+logo.path
	tag_search = request.GET.get("tag_search","").strip().replace(" ",",")
	tags_list = tag_search.split(",")
	userinfo = request.session.get("userinfo",default=None)
	banners = Banner.objects.filter(status=1).order_by('-id').all()[:4]
	if tags_list[0] != "":
		spnews_list = []
		nid = []
		for tag in tags_list:
			# print"------------------------",tag
			for news in list(Spnews.objects.filter(tags__icontains=tag,status=1).all()):
				if (news.id in nid):
					pass
				else:
					nid.append(news.id)
					spnews_list.append(news)
		if len(spnews_list) == 0:
			spnews_list = Spnews.objects.filter(status=1).order_by('-id').all()
	else:
		spnews_list = Spnews.objects.filter(ntype=1,status=1).order_by('-id').all()
	page_size = 10
	after_range_num = 5
	before_range_num = 6
	try:
		page = int(request.GET.get("page",1))
		if page < 1:
			page = 1
	except ValueError:
		page = 1
	paginator = Paginator(spnews_list,page_size)
	try:
		news = paginator.page(page)
	except (EmptyPage,InvalidPage,PageNotAnInteger):
		news = paginator.page(1)
	if page >=after_range_num:
		page_range = paginator.page_range[page-after_range_num:page+before_range_num]
	else:
		page_range = paginator.page_range[0:int(page)+before_range_num]

	results = {"userinfo":userinfo,"logo":logo_path,"banners":banners,"news":news,"page_range":page_range,"tag_search":tag_search}
	return render(request, 'sipingxinwen.html',{"response":results})

def zainishenbian(request):
	logoList = Splogo.objects.filter(status=1).all()[:1]
	if logoList.count() == 0:
		logo_path = "/static/style/imgs/logo.png"
	else:
		for logo in logoList:
			logo_path = "/static/media/logo/"+logo.path
	tag_search = request.GET.get("tag_search","").strip().replace(" ",",")
	tags_list = tag_search.split(",")
	userinfo = request.session.get("userinfo",default=None)
	banners = Banner.objects.filter(status=1).order_by('-id').all()[:4]
	if tags_list[0] != "":
		spnews_list = []
		nid = []
		for tag in tags_list:
			# print"------------------------",tag
			for news in list(Spnews.objects.filter(tags__icontains=tag,status=1).all()):
				if (news.id in nid):
					pass
				else:
					nid.append(news.id)
					spnews_list.append(news)
		if len(spnews_list) == 0:
			spnews_list = Spnews.objects.filter(status=1).order_by('-id').all()
	else:
		spnews_list = Spnews.objects.filter(ntype=2,status=1).order_by('-id').all()
	page_size = 10
	after_range_num = 5
	before_range_num = 6
	try:
		page = int(request.GET.get("page",1))
		if page < 1:
			page = 1
	except ValueError:
		page = 1
	paginator = Paginator(spnews_list,page_size)
	try:
		news = paginator.page(page)
	except (EmptyPage,InvalidPage,PageNotAnInteger):
		news = paginator.page(1)
	if page >=after_range_num:
		page_range = paginator.page_range[page-after_range_num:page+before_range_num]
	else:
		page_range = paginator.page_range[0:int(page)+before_range_num]

	results = {"userinfo":userinfo,"logo":logo_path,"banners":banners,"news":news,"page_range":page_range,"tag_search":tag_search}
	return render(request, 'zainishenbian.html',{"response":results})

def xianquxinwen(request):
	logoList = Splogo.objects.filter(status=1).all()[:1]
	if logoList.count() == 0:
		logo_path = "/static/style/imgs/logo.png"
	else:
		for logo in logoList:
			logo_path = "/static/media/logo/"+logo.path
	tag_search = request.GET.get("tag_search","").strip().replace(" ",",")
	tags_list = tag_search.split(",")
	userinfo = request.session.get("userinfo",default=None)
	banners = Banner.objects.filter(status=1).order_by('-id').all()[:4]
	if tags_list[0] != "":
		spnews_list = []
		nid = []
		for tag in tags_list:
			# print"------------------------",tag
			for news in list(Spnews.objects.filter(tags__icontains=tag,status=1).all()):
				if (news.id in nid):
					pass
				else:
					nid.append(news.id)
					spnews_list.append(news)
		if len(spnews_list) == 0:
			spnews_list = Spnews.objects.filter(status=1).order_by('-id').all()
	else:
		spnews_list = Spnews.objects.filter(ntype=3,status=1).order_by('-id').all()
	page_size = 10
	after_range_num = 5
	before_range_num = 6
	try:
		page = int(request.GET.get("page",1))
		if page < 1:
			page = 1
	except ValueError:
		page = 1
	paginator = Paginator(spnews_list,page_size)
	try:
		news = paginator.page(page)
	except (EmptyPage,InvalidPage,PageNotAnInteger):
		news = paginator.page(1)
	if page >=after_range_num:
		page_range = paginator.page_range[page-after_range_num:page+before_range_num]
	else:
		page_range = paginator.page_range[0:int(page)+before_range_num]

	results = {"userinfo":userinfo,"logo":logo_path,"banners":banners,"news":news,"page_range":page_range,"tag_search":tag_search}
	return render(request, 'xianquxinwen.html',{"response":results})

def shipinzhanbo(request):
	logoList = Splogo.objects.filter(status=1).all()[:1]
	if logoList.count() == 0:
		logo_path = "/static/style/imgs/logo.png"
	else:
		for logo in logoList:
			logo_path = "/static/media/logo/"+logo.path
	tag_search = request.GET.get("tag_search","").strip().replace(" ",",")
	tags_list = tag_search.split(",")
	userinfo = request.session.get("userinfo",default=None)
	banners = Banner.objects.filter(status=1).order_by('-id').all()[:4]
	if tags_list[0] != "":
		spnews_list = []
		nid = []
		for tag in tags_list:
			# print"------------------------",tag
			for news in list(Spnews.objects.filter(tags__icontains=tag,status=1).all()):
				if (news.id in nid):
					pass
				else:
					nid.append(news.id)
					spnews_list.append(news)
		if len(spnews_list) == 0:
			spnews_list = Spnews.objects.filter(status=1).order_by('-id').all()
	else:
		spnews_list = Spnews.objects.filter(ntype=4,status=1).order_by('-id').all()
	page_size = 9
	after_range_num = 5
	before_range_num = 6
	try:
		page = int(request.GET.get("page",1))
		if page < 1:
			page = 1
	except ValueError:
		page = 1
	paginator = Paginator(spnews_list,page_size)
	try:
		news = paginator.page(page)
	except (EmptyPage,InvalidPage,PageNotAnInteger):
		news = paginator.page(1)
	if page >=after_range_num:
		page_range = paginator.page_range[page-after_range_num:page+before_range_num]
	else:
		page_range = paginator.page_range[0:int(page)+before_range_num]

	results = {"userinfo":userinfo,"logo":logo_path,"banners":banners,"news":news,"page_range":page_range,"tag_search":tag_search}
	return render(request, 'shipinzhanbo.html',{"response":results})

def jingpinlanmu(request):
	ntype = int(request.GET.get("ntype",4))
	logoList = Splogo.objects.filter(status=1).all()[:1]
	if logoList.count() == 0:
		logo_path = "/static/style/imgs/logo.png"
	else:
		for logo in logoList:
			logo_path = "/static/media/logo/"+logo.path
	tag_search = request.GET.get("tag_search","").strip().replace(" ",",")
	tags_list = tag_search.split(",")
	userinfo = request.session.get("userinfo",default=None)
	banners = Banner.objects.filter(status=1).order_by('-id').all()[:4]
	spgroup_list = Spgroup.objects.filter(status=1,gtype=2).order_by('-id').all()
	# spnews_list = {}
	spnews_list2 = {}
	for spgroup in spgroup_list:
		spnews_list2[spgroup.id] = list(Spnews.objects.filter(status=1,ntype=spgroup.id).order_by('-id').all()[:3])
		print "-------------------------"+ str(len(spnews_list2[spgroup.id]))
	page_size = 10
	after_range_num = 5
	before_range_num = 6
	try:
		page = int(request.GET.get("page",1))
		if page < 1:
			page = 1
	except ValueError:
		page = 1
	paginator = Paginator(spgroup_list,page_size)
	try:
		spgroup = paginator.page(page)
	except (EmptyPage,InvalidPage,PageNotAnInteger):
		spgroup = paginator.page(1)
	if page >=after_range_num:
		page_range = paginator.page_range[page-after_range_num:page+before_range_num]
	else:
		page_range = paginator.page_range[0:int(page)+before_range_num]
	# print spnews_list
	results = {"userinfo":userinfo,"logo":logo_path,"banners":banners,"spgroup":spgroup,"spnews_list2":spnews_list2,"page_range":page_range}
	return render(request, 'jingpinlanmu.html',{"response":results})


def xinwenbofangitem(request):
	logoList = Splogo.objects.filter(status=1).all()[:1]
	if logoList.count() == 0:
		logo_path = "/static/style/imgs/logo.png"
	else:
		for logo in logoList:
			logo_path = "/static/media/logo/"+logo.path
	userinfo = request.session.get("userinfo",default=None)
	nid = int(request.GET.get('nid','0').strip())
	ntype = int(request.GET.get("ntype","1").strip())
	if nid ==0:
		raw_sql = 'select * from spnews where status=1 order by id desc ;';
		for h in Spnews.objects.raw(raw_sql):
			news = h
			break
	else:
		news = Spnews.objects.get(id=nid)
	news.read_num = news.read_num + 1
	news.save()
	# news.media_path = str(news.media_path).split(".")[0]+"/1/mp4/1_1."+str(news.media_path).split(".")[1]
	tags_list = news.tags.split(",")
	glnews_list = []
	nid_list = []
	for tag in tags_list:
		glnews_list_temp = list(Spnews.objects.filter(status=1,tags__icontains=tag).order_by('-id').all()[:4])
		for glnews in glnews_list_temp:
			if (news.id in nid_list) or news.id == nid:
				pass
			else:
				nid_list.append(news.id)
				glnews_list.append(glnews)
	if len(glnews_list)<4:
		glnews_list.extend(list(Spnews.objects.filter(status=1).exclude(id=nid).order_by('-id').all()[:4-len(glnews_list)]))
	print nid_list
	for gl in glnews_list:
		gl.media_path = str(gl.media_path).split(".")[0]+"/1/mp4/1_1."+str(gl.media_path).split(".")[1]
	lnews_list = Spnews.objects.filter(status=1).order_by("-id").all()
	page_size = 10
	after_range_num = 5
	before_range_num = 6
	try:
		page = int(request.GET.get("page",1))
		if page < 1:
			page = 1
	except ValueError:
		page = 1
	paginator = Paginator(lnews_list,page_size)
	try:
		lnews = paginator.page(page)
	except (EmptyPage,InvalidPage,PageNotAnInteger):
		lnews = paginator.page(1)
	if page >=after_range_num:
		page_range = paginator.page_range[page-after_range_num:page+before_range_num]
	else:
		page_range = paginator.page_range[0:int(page)+before_range_num]

	# for x in xrange(0,4-len(glnews_list)):
	# 	glnews_list.append(lnews_list[5+x])
	
	results = {"userinfo":userinfo,"logo":logo_path,"news":news,"glnews_list":glnews_list,"lnews_list":lnews,"page_range":page_range}
	return render(request, 'xinwenbofangitem.html',{"response":results})

def jingpinzhanboitem(request):
	logoList = Splogo.objects.filter(status=1).all()[:1]
	if logoList.count() == 0:
		logo_path = "/static/style/imgs/logo.png"
	else:
		for logo in logoList:
			logo_path = "/static/media/logo/"+logo.path
	userinfo = request.session.get("userinfo",default=None)
	nid = int(request.GET.get('nid','0').strip())
	ntype = int(request.GET.get("ntype","1").strip())
	if nid ==0:
		raw_sql = 'select * from spnews where status=1 order by id desc ;';
		for h in Spnews.objects.raw(raw_sql):
			news = h
			break
	else:
		news = Spnews.objects.get(id=nid)
	news.read_num = news.read_num + 1
	news.save()
	# news.media_path = str(news.media_path).split(".")[0]+"/1/mp4/1_1."+str(news.media_path).split(".")[1]
	tags_list = news.tags.split(",")
	glnews_list = []
	nid = []
	for tag in tags_list:
		glnews_list_temp = list(Spnews.objects.filter(status=1,tags__icontains=tag).order_by('-id').all()[:4])
		for glnews in glnews_list_temp:
			if (news.id in nid):
				pass
			else:
				nid.append(news.id)
				glnews_list.append(glnews)
	if len(glnews_list)<4:
		glnews_list.extend(list(Spnews.objects.filter(status=1).order_by('-id').all()[:4-len(glnews_list)])) 
	for gl in glnews_list:
		gl.media_path = str(gl.media_path).split(".")[0]+"/1/mp4/1_1."+str(gl.media_path).split(".")[1]
	lnews_list = Spnews.objects.filter(status=1).order_by("-id").all()
	page_size = 9
	after_range_num = 5
	before_range_num = 6
	try:
		page = int(request.GET.get("page",1))
		if page < 1:
			page = 1
	except ValueError:
		page = 1
	paginator = Paginator(lnews_list,page_size)
	try:
		lnews = paginator.page(page)
	except (EmptyPage,InvalidPage,PageNotAnInteger):
		lnews = paginator.page(1)
	if page >=after_range_num:
		page_range = paginator.page_range[page-after_range_num:page+before_range_num]
	else:
		page_range = paginator.page_range[0:int(page)+before_range_num]
	# for x in xrange(0,4-len(glnews_list)):
	# 	glnews_list.append(lnews_list[5+x])
	
	results = {"userinfo":userinfo,"logo":logo_path,"news":news,"glnews_list":glnews_list,"lnews_list":lnews,"page_range":page_range}
	return render(request, 'jingpinzhanboitem.html',{"response":results})

def gonggaolist(request):
	logoList = Splogo.objects.filter(status=1).all()[:1]
	if logoList.count() == 0:
		logo_path = "/static/style/imgs/logo.png"
	else:
		for logo in logoList:
			logo_path = "/static/media/logo/"+logo.path
	userinfo = request.session.get("userinfo",default=None)
	banners = Banner.objects.filter(status=1).order_by('-id').all()[:4]
	gonggao_list = Gonggao.objects.filter(status=1).order_by('-id').all()
	page_size = 10
	after_range_num = 5
	before_range_num = 6
	try:
		page = int(request.GET.get("page",1))
		if page < 1:
			page = 1
	except ValueError:
		page = 1
	paginator = Paginator(gonggao_list,page_size)
	try:
		gonggao = paginator.page(page)
	except (EmptyPage,InvalidPage,PageNotAnInteger):
		gonggao = paginator.page(1)
	if page >=after_range_num:
		page_range = paginator.page_range[page-after_range_num:page+before_range_num]
	else:
		page_range = paginator.page_range[0:int(page)+before_range_num]
	print gonggao.object_list
	results = {"userinfo":userinfo,"logo":logo_path,"banners":banners,"gonggao":gonggao,"page_range":page_range}
	return render(request, 'gonggaolist.html',{"response":results})

def gonggaoitem(request):
	gid = request.GET.get("gid",1)
	logoList = Splogo.objects.filter(status=1).all()[:1]
	if logoList.count() == 0:
		logo_path = "/static/style/imgs/logo.png"
	else:
		for logo in logoList:
			logo_path = "/static/media/logo/"+logo.path
	userinfo = request.session.get("userinfo",default=None)
	banners = Banner.objects.filter(status=1).order_by('-id').all()[:4]
	gonggao = Gonggao.objects.get(status=1,id=gid)
	
	results = {"userinfo":userinfo,"logo":logo_path,"banners":banners,"gonggao":gonggao}
	return render(request, 'gonggaoitem.html',{"response":results})

def zhuanlanxuanchuan(request):
	logoList = Splogo.objects.filter(status=1).all()[:1]
	if logoList.count() == 0:
		logo_path = "/static/style/imgs/logo.png"
	else:
		for logo in logoList:
			logo_path = "/static/media/logo/"+logo.path
	userinfo = request.session.get("userinfo",default=None)
	banners = Banner.objects.filter(status=1).order_by('-id').all()[:4]
	spgroup_list = Spgroup.objects.filter(status=1,gtype=3).order_by('-id').all()
	# spnews_list = {}
	# for spgroup in spgroup_list:
	# 	spgroup['spnews'] = list(Spnews.objects.filter(status=1,ntype=spgroup.id).order_by('-id').all()[:10])
	page_size = 10
	after_range_num = 5
	before_range_num = 6
	try:
		page = int(request.GET.get("page",1))
		if page < 1:
			page = 1
	except ValueError:
		page = 1
	paginator = Paginator(spgroup_list,page_size)
	try:
		spgroup = paginator.page(page)
	except (EmptyPage,InvalidPage,PageNotAnInteger):
		spgroup = paginator.page(1)
	if page >=after_range_num:
		page_range = paginator.page_range[page-after_range_num:page+before_range_num]
	else:
		page_range = paginator.page_range[0:int(page)+before_range_num]
	# print spnews_list
	results = {"userinfo":userinfo,"logo":logo_path,"banners":banners,"spgroup":spgroup,"page_range":page_range}
	return render(request, 'zhuanlanlist.html',{"response":results})

def huodongtoupiao(request):
	logoList = Splogo.objects.filter(status=1).all()[:1]
	if logoList.count() == 0:
		logo_path = "/static/style/imgs/logo.png"
	else:
		for logo in logoList:
			logo_path = "/static/media/logo/"+logo.path
	userinfo = request.session.get("userinfo",default=None)
	banners = Banner.objects.filter(status=1).order_by('-id').all()[:4]
	hid = int(request.GET.get("hid","0"))
	if hid ==0:
		raw_sql = 'select * from huodong where status=1 order by id desc ;';
		for h in Huodong.objects.raw(raw_sql):
			huodong = h
			break
	else:
		huodong = Huodong.objects.get(id=hid)
	news_list = Spnews.objects.filter(status=1,huodongid=huodong.id).all()
	results = {"userinfo":userinfo,"logo":logo_path,"banners":banners,"huodong":huodong,"news_list":news_list}
	return render(request, 'huodongtoupiao.html',{"response":results})

def addzan(request):
	try:
		nid = request.GET.get("nid","0")
		coostr = request.GET.get("coostr","").split(":")[1]
		nid_list = coostr.split(",")
		# print nid_list
		if request.META.has_key('HTTP_X_FORWARDED_FOR'):  
			ip =  request.META['HTTP_X_FORWARDED_FOR']  
		else:  
	    		ip = request.META['REMOTE_ADDR']
		if nid ==0:
			results = {
				"resCode":2,
				"resDesc":"投票失败"
			}
		elif nid in nid_list:
			results = {
				"resCode":2,
				"resDesc":"请勿重复投票"
			}
		else:
			news = Spnews.objects.get(id=nid)
			if Toupiaoyanzheng.objects.filter(huodongid=news.huodongid,spnewsid=news.id,ip=ip).count()>0:
				results = {
				"resCode":2,
				"resDesc":"请勿重复投票"
			}
			else:
				toupiao = Toupiaoyanzheng(huodongid=news.huodongid,spnewsid=news.id,ip=ip,createtime=str(datetime.now())[:19])
				toupiao.save()
				news.zan_num = news.zan_num + 1
				news.save()
				results = {
					"resCode":1,
					"resDesc":"投票成功"
				}
		# print ip
		# results={}
	except Exception, e:
		logger = logging.getLogger('siping')
		logger.info(str(e))
		results = {
			"resCode":500,
			"resDesc":"服务器异常"
		}
	return HttpResponse(json.dumps(results), content_type='application/json')

def presenter(request):
	return render(request, 'presenter.html',)

def tologin(request):
	userinfo = request.session.get("userinfo",default=None)
	results = {"userinfo":userinfo}
	return render(request, 'slogin.html', {"response":results,})

def toregist(request):
	userinfo = request.session.get("userinfo",default=None)
	results = {"userinfo":userinfo}
	return render(request, 'sregister.html', {"response":results})


def register(request):
	try:
		username =request.POST.get('username','').strip()
		cellphone = request.POST.get('cellphone','').strip()
		email = request.POST.get('email','').strip()
		password = request.POST.get('password','').strip()
		if username != "" or password != "":
			users1 = User.objects.filter(username=username).count()
			users2 = User.objects.filter(cellphone=cellphone).count()
			users3 = User.objects.filter(email=email).count()
			if users1 >0:
				results = {
					"resCode":2,
					"resDesc":"用户名已被注册"
				}
			elif users2 > 0:
				results = {
					"resCode":2,
					"resDesc":"手机号已被注册"
				}
			elif users3 > 0:
				results = {
					"resCode":2,
					"resDesc":"邮箱已经被注册"
				}
			else:
				pwd_md5=hashlib.md5(password.encode('utf-8')).hexdigest()
				user = User()
				user.username = username
				user.password = pwd_md5
				user.cellphone = cellphone
				user.email = email
				user.right = 10
				user.save()
				userinfo = {}
				userinfo['username'] = username
				userinfo['sex'] = 0
				userinfo['right'] = 10
				userinfo['nick'] = '' 
				request.session['userinfo'] = userinfo
				results = {
					"resCode":1,
					"resDesc":"用户名注册成功"
				}
		else:
			 results = {
				"resCode":0,
				"resDesc":"用户名或密码不能为空"
			}
	except Exception, e:
		logger = logging.getLogger('siping')
		logger.info(str(e))
		results = {
			"resCode":500,
			"resDesc":"服务器异常"
		}
	return HttpResponse(json.dumps(results), content_type='application/json')
	# return render_template("companyDetail.html")


def login(request):
	try:
		username =request.POST.get('username','').strip()
		password = request.POST.get('password','').strip()
		pwd_md5=hashlib.md5(password.encode('utf-8')).hexdigest()
		flag = True
		if username != "" or password != "":
			if User.objects.filter(username=username).count()>0:
				users = User.objects.filter(username=username,password=pwd_md5)
			elif User.objects.filter(cellphone=username).count()>0:
				users = User.objects.filter(cellphone=username,password=pwd_md5)
			elif User.objects.filter(email=username).count() > 0:
				users = User.objects.filter(email=username,password=pwd_md5)
			else:
				flag = False
				results = {
					"resCode":2,
					"resDesc":"用户未注册"
				}
			if flag ==False:
				pass
			else:
				if len(users) == 0:
					results = {
						"resCode":3,
						"resDesc":"密码不正确!"
					}
				else:
					for user in users:
						userinfo = {
							"username":user.username,
							"sex":user.sex,
							"right":user.right,
							"nickname":user.nickname,
						}
					request.session['userinfo'] = userinfo
					results = {
						"resCode":1,
						"resDesc":"用户名登录成功"
					}
				
		else:
			 results = {
				"resCode":0,
				"resDesc":"用户名或密码不能为空"
			}
	except Exception, e:
		logger = logging.getLogger('siping')
		logger.info(str(e))
		results = {
			"resCode":500,
			"resDesc":"服务器异常" 
		}
	return HttpResponse(json.dumps(results), content_type='application/json')
	
def logout(request):
	userinfo = request.session.get('userinfo',default=None)
	if userinfo != None:
		del request.session['userinfo'] # 不存在时报错
	data = {
		"userinfo":userinfo,
	}
	data = {"userinfo":userinfo,}
	return HttpResponseRedirect("/index") 


def getNewsList(request):
	try:
		ntype =int(request.GET.get('ntype',"1").strip())
		pagenum =int(request.GET.get('pagenum',"0").strip())
		spnews_list = Spnews.objects.filter(ntype=ntype,status=1)[:10]
		data = []
		for spnews in spnews_list:
			data.append(
				{
					"id":spnews.id,
					"title":spnews.title,
					"shot_content":spnews.shot_content,
					"src":spnews.src,
					"createtime":spnews.createtime.strftime("%Y年%m月%d日"),
					"image_media_path":str(spnews.image_media_path),
					"media_path":str(spnews.media_path)
				}
			)
		results = {
			"pagenum":pagenum,
			"news" :data
		}
	except Exception, e:
		logger = logging.getLogger('siping')
		logger.info(str(e))
		results = {
			"resCode":500,
			"resDesc":"服务器异常"
		}
	return HttpResponse(json.dumps(results), content_type='application/json')