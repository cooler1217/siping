# coding=utf-8
from __future__ import unicode_literals
from django.db import models

import datetime
# Create your models here.


class Group(models.Model):
    groupname = models.CharField(max_length=100)
    groupright = models.IntegerField()
    desc = models.CharField(max_length=145, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'group'


class Presenter(models.Model):
    name = models.CharField(max_length=145, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    department = models.CharField(max_length=145, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    lastmodify = models.DateTimeField(blank=True, null=True)
    head_image = models.FileField(upload_to = './static/media/presenter/',max_length=145,blank=True)
    abstract = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=145, blank=True, null=True)
    read_num = models.IntegerField(blank=True, null=True)
    zan_num = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ntype = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'presenter'


class Spnews(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)#标题
    shot_content = models.CharField(max_length=200, blank=True, null=True)#简介
    content = models.TextField(blank=True, null=True)#内容
    createtime = models.DateTimeField(blank=True, null=True)
    lastmodify = models.DateTimeField(blank=True, null=True)
    read_num = models.IntegerField(blank=True, null=True)#阅读次数
    zan_num = models.IntegerField(blank=True, null=True)#点赞的次数
    author = models.CharField(max_length=145, blank=True, null=True) #作者
    src = models.CharField(max_length=145, blank=True, null=True)#来源
    reporter = models.CharField(max_length=145, blank=True, null=True)#
    desc = models.CharField(max_length=145, blank=True, null=True)#描述
    image_media_path = models.FileField(upload_to = './static/media/spnews/head_image/',max_length=255,blank=True)　#资源图片
    media_path = models.FileField(upload_to = './static/media/spnews/shipin/',max_length=255,blank=True)　#资源地址
    ntype = models.IntegerField(blank=True, null=True)#新闻类型
    status = models.IntegerField(blank=True, null=True)#新闻状态 0  新上传　 1 正常显示 2 审核失败
    tags = models.CharField(max_length=145, blank=True, null=True)　#　标签，关联视频
    zebian = models.CharField(max_length=145, blank=True, null=True) # 责任编辑

    class Meta:
        # managed = False
        db_table = 'spnews'


class User(models.Model):
    username = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    right = models.IntegerField(blank=True, null=True)
    groupid = models.IntegerField(blank=True, null=True)
    real_name = models.CharField(max_length=45, blank=True, null=True)
    birthday = models.CharField(max_length=45, blank=True, null=True)
    cellphone = models.CharField(max_length=45, blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    nickname = models.CharField(max_length=45, blank=True, null=True)
    idcard = models.CharField(max_length=45, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    lastmodify = models.DateTimeField(blank=True, null=True)
    verify_code = models.CharField(max_length=45, blank=True, null=True)
    addip = models.CharField(max_length=45, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'user'


class Banner(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    desc = models.CharField(max_length=45, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    image_path = models.FileField(upload_to = './static/media/banner/',max_length=145, blank=True, null=True)
    uri = models.CharField(max_length=245, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'banner'