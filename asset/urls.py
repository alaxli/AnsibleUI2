#!usr/bin/env python
# coding:utf-8

from django.conf.urls import url
from asset import views

__author__ = 'sunyaxiong'


urlpatterns = [
    url(r'^list', views.node_list, name='node_list'),
]
