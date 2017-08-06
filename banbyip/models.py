# -*- coding: utf-8 -*-
from django.db import models

import random
from django.conf import settings

import datetime
import random




class Ip(models.Model):
    ip = models.CharField(max_length=250, default="", blank=True, db_index=True, verbose_name="Ip")
    count = models.IntegerField(verbose_name="Количество заходов", default=0, blank=True, null=True)
    ban = models.BooleanField(verbose_name="Исключен", default=0)
    g = models.IntegerField(verbose_name="Google", default=0, blank=True, null=True)
    y = models.IntegerField(verbose_name="Yandex", default=0, blank=True, null=True)
    def __unicode__(self):
        return self.ip
    class Meta:
        verbose_name_plural = u"Ip"


class Users(models.Model):
    ip = models.ManyToManyField(Ip, blank=True)
    ips = models.CharField(max_length=250, default="", blank=True, verbose_name="Ip")
    name = models.CharField(max_length=250, default="", blank=True, db_index=True, verbose_name="Название")
    ban = models.BooleanField(verbose_name="Исключен", default=0)
    g = models.IntegerField(verbose_name="Google", default=0, blank=True, null=True)
    y = models.IntegerField(verbose_name="Yandex", default=0, blank=True, null=True)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = u"Users"



class Visit(models.Model):
    user = models.ForeignKey(Users,null=True, blank=True, verbose_name="User")
    ip = models.CharField(max_length=250, default="", blank=True, db_index=True, verbose_name="Ip")
    ref = models.CharField(max_length=250, default="", blank=True, db_index=True, verbose_name="Ref")
    ref2 = models.TextField( default="", blank=True,  verbose_name="Ref")
    agent = models.CharField(max_length=250, default="", blank=True, db_index=True, verbose_name="Agent")
    host = models.CharField(max_length=250, default="", blank=True, db_index=True, verbose_name="Host")
    qu = models.CharField(max_length=250, default="", blank=True, db_index=True, verbose_name="Запрос")
    data = models.DateTimeField(null=True,auto_now_add=True)
    def __unicode__(self):
        return self.ip
    class Meta:
        verbose_name_plural = u"Visit"
