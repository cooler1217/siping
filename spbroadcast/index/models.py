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
    title = models.CharField(max_length=100, blank=True, null=True)
    shot_content = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    lastmodify = models.DateTimeField(blank=True, null=True)
    read_num = models.IntegerField(blank=True, null=True)
    zan_num = models.IntegerField(blank=True, null=True)
    author = models.CharField(max_length=145, blank=True, null=True) 
    src = models.CharField(max_length=145, blank=True, null=True)
    reporter = models.CharField(max_length=145, blank=True, null=True)
    desc = models.CharField(max_length=145, blank=True, null=True)
    image_media_path = models.FileField(upload_to = './static/media/spnews/head_image/',max_length=255,blank=True)
    media_path = models.FileField(upload_to = './static/media/spnews/shipin/',max_length=255,blank=True)
    ntype = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    tags = models.CharField(max_length=145, blank=True, null=True)
    zebian = models.CharField(max_length=145, blank=True, null=True) 
    huodongid = models.IntegerField(blank=True, null=True)

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
    email = models.CharField(max_length=145, blank=True, null=True)

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

class Fengmian(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=45, blank=True, null=True)
    path = models.CharField(max_length=145, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    lastmodify = models.DateTimeField(blank=True, null=True)
    desc = models.CharField(max_length=145, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'fengmian'


class Shipin(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=145, blank=True, null=True)
    path = models.CharField(max_length=145, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    lastmodify = models.DateTimeField(blank=True, null=True)
    desc = models.CharField(max_length=145, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'shipin'

class Huodong(models.Model):
    name = models.CharField(max_length=245, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    starttime = models.IntegerField(blank=True, null=True)
    endtime = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    author = models.CharField(max_length=145, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    lastmodify = models.DateTimeField(blank=True, null=True)
    file_path = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'huodong'

class Toupiaoyanzheng(models.Model):
    huodongid = models.IntegerField(blank=True, null=True)
    spnewsid = models.IntegerField(blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=145, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    lastmodify = models.DateTimeField(blank=True, null=True)
    tptime = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'toupiaoyanzheng'

class Splogo(models.Model):
    name = models.CharField(max_length=145, blank=True, null=True)
    path = models.CharField(max_length=145, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    desc = models.CharField(max_length=145, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'splogo'

class Gonggao(models.Model):
    title = models.CharField(max_length=145, blank=True, null=True)
    content = models.CharField(max_length=145, blank=True, null=True)
    author = models.CharField(max_length=145, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    image_path = models.CharField(max_length=145, blank=True, null=True)
    url = models.CharField(max_length=245, blank=True, null=True)
    gtype = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'gonggao'


class Spgroup(models.Model):
    name = models.CharField(max_length=145, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    image_path = models.CharField(max_length=145, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    desc = models.CharField(max_length=245, blank=True, null=True)
    gtype = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'spgroup'