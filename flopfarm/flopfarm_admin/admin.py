'''
Author: your name
Date: 2021-04-29 21:25:00
LastEditTime: 2021-05-02 17:53:51
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /FlopFarmAdminLTE/flopfarm/flopfarm_admin/admin.py
'''
from django.contrib import admin

# Register your models here.

from .models import Instance

admin.site.register(Instance)