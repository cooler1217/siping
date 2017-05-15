"""spbroadcast URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^regist/$', 'index.views.register', name='home'),# Notice this line
    url(r'^login/$', 'index.views.login', name='home'),# Notice this line
    url(r'^tologin/$', 'index.views.tologin', name='home'),# Notice this line
    url(r'^toregist/$', 'index.views.toregist', name='home'),# Notice this line
    url(r'^logout/$', 'index.views.logout', name='home'),# Notice this line

    url(r'^getNewsList/$', 'index.views.getNewsList', name='home'),# Notice this line

    url(r'^cooler/$', 'index.views.cooler', name='home'),# Notice this line
    url(r'^$', 'index.views.index', name='home'),# Notice this line
    url(r'^index/$', 'index.views.index', name='home'),# Notice this line
    url(r'^sipingxinwen/$', 'index.views.sipingxinwen', name='home'),# Notice this line
    url(r'^xianquxinwen/$', 'index.views.xianquxinwen', name='home'),# Notice this line
    url(r'^zainishenbian/$', 'index.views.zainishenbian', name='home'),# Notice this line
    url(r'^zainishenbian/$', 'index.views.zainishenbian', name='home'),# Notice this line
    url(r'^gonggaolist/$', 'index.views.gonggaolist', name='home'),# Notice this line
    url(r'^gonggaoitem/$', 'index.views.gonggaoitem', name='home'),# Notice this line
    url(r'^jingpinlanmu/$', 'index.views.jingpinlanmu', name='home'),# Notice this line
    url(r'^zhuanlanxuanchuan/$', 'index.views.zhuanlanxuanchuan', name='home'),# Notice this line
    url(r'^xinwenbofangitem/$', 'index.views.xinwenbofangitem', name='home'),# Notice this line
    url(r'^jingpinzhanboitem/$', 'index.views.jingpinzhanboitem', name='home'),# Notice this line
    url(r'^huodongtoupiao/$', 'index.views.huodongtoupiao', name='home'),# Notice this line
    url(r'^addzan/$', 'index.views.addzan', name='home'),# Notice this line
    url(r'^presenter/$', 'index.views.presenter', name='home'),# Notice this line
]
