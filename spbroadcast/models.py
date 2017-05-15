# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Banner(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    desc = models.CharField(max_length=45, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    image_path = models.CharField(max_length=145, blank=True, null=True)
    uri = models.CharField(max_length=245, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banner'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Fengmian(models.Model):
    title = models.CharField(max_length=145, blank=True, null=True)
    path = models.CharField(max_length=145, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    lastmodify = models.DateTimeField(blank=True, null=True)
    desc = models.CharField(max_length=145, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fengmian'


class Group(models.Model):
    groupname = models.CharField(max_length=100)
    groupright = models.IntegerField()
    desc = models.CharField(max_length=145, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group'


class Huodong(models.Model):
    name = models.CharField(max_length=245, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    starttime = models.IntegerField(blank=True, null=True)
    endtime = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    author = models.CharField(max_length=145, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    lastmodify = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'huodong'


class Presenter(models.Model):
    name = models.CharField(max_length=145, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    department = models.CharField(max_length=145, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    lastmodify = models.DateTimeField(blank=True, null=True)
    head_image = models.CharField(max_length=145)
    abstract = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=145, blank=True, null=True)
    read_num = models.IntegerField(blank=True, null=True)
    zan_num = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ntype = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'presenter'


class Shipin(models.Model):
    title = models.CharField(max_length=145, blank=True, null=True)
    path = models.CharField(max_length=145, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    lastmodify = models.DateTimeField(blank=True, null=True)
    desc = models.CharField(max_length=145, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipin'


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
    image_media_path = models.CharField(max_length=255)
    media_path = models.CharField(max_length=255)
    ntype = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    tags = models.CharField(max_length=45, blank=True, null=True)
    zebian = models.CharField(max_length=145, blank=True, null=True)
    huodongid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spnews'


class Toupiaoyanzheng(models.Model):
    huodongid = models.IntegerField(blank=True, null=True)
    spnewsid = models.IntegerField(blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=145, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    lastmodify = models.DateTimeField(blank=True, null=True)
    tptime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'toupiaoyanzheng'


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
        managed = False
        db_table = 'user'
