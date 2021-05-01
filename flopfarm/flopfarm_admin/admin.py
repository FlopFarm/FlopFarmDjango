'''
Author: your name
Date: 2021-04-29 21:25:00
LastEditTime: 2021-05-01 23:35:46
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /FlopFarmAdminLTE/flopfarm/flopfarm_admin/admin.py
'''
from django.contrib import admin

# Register your models here.

from .models import EdgeProvider, User, Instance

admin.site.register(User)
admin.site.register(Instance)
admin.site.register(EdgeProvider)