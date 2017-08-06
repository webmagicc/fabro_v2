# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import *

from django.db import models

class IpAdmin(admin.ModelAdmin):

    list_display = ('ip', 'count', 'g','y', 'ban')
    list_editable = ('ban',)


class UsersAdmin(admin.ModelAdmin):

    list_display = ('name', 'ips','g','y', 'ban')
    list_editable = ('ban',)



class VisitAdmin(admin.ModelAdmin):

    list_display = ('user', 'id', 'data', 'ip', 'ref2', 'agent', 'qu', 'host')
    search_fields = ('ip','user__name')





admin.site.register(Ip, IpAdmin)
admin.site.register(Visit, VisitAdmin)

admin.site.register(Users, UsersAdmin)
