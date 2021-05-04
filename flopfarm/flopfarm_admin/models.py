'''
Author: your name
Date: 2021-04-29 21:25:00
LastEditTime: 2021-05-04 13:21:23
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /FlopFarmAdminLTE/flopfarm/flopfarm_admin/models.py
'''
from django.db import models
import uuid
from django.contrib.auth.models import User
import datetime
class Instance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular instance')
    name = models.CharField(max_length=200, help_text='Enter the instance name')
    
    TYPE = (
        ('c', 'General Computing Instance'),
        ('d', 'Deep Learning API')
    )

    STATUS = (
        ('i', 'Idle'),
        ('r', 'Running'),
    )

    type = models.CharField(
        max_length=1, 
        choices = TYPE, 
        blank = True, 
        default = 'c', 
        help_text='Instance type'
    )

    status = models.CharField(
        max_length=1, 
        choices = STATUS, 
        blank = True, 
        default = 'i', 
        help_text='Instance status'
    )

    OS = models.CharField(max_length=200, blank = True, null = True, help_text='Enter the Operating System info')
    CPU = models.CharField(max_length=200, blank = True, null = True, help_text='Enter the CPU info')
    GPU = models.CharField(max_length=200, blank = True, null = True, help_text='Enter the GPU info')
    RAM = models.CharField(max_length=200, blank = True, null = True, help_text='Enter the RAM info')
    hourly_price = models.FloatField(blank = True, null = True, help_text='Enter the hourly price')
    s_time = models.DateTimeField(blank = True, null = True, help_text = 'Start running time')
    e_time = models.DateTimeField(blank = True, null = True, help_text = 'end running time')
    IP = models.CharField(max_length=200, blank = True, null = True, help_text='Enter IP')
    username = models.CharField(max_length=200, blank = True, null = True, help_text='Enter SSH user name')
    password = models.CharField(max_length=200, blank = True, null = True, help_text='Enter SSH password')

    APIinfo = models.CharField(max_length=200,blank = True, null = True, help_text='Enter the API info')
    API_price = models.FloatField(blank = True, null = True, help_text='Enter the price per use for API')

    remarks = models.CharField(max_length=200, blank = True, null = True, help_text='Enter the remarks')

    provider = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='Instance_provided')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null=True, related_name='Instance_using')

    def get_remaining_time(self):
        tzinfo = datetime.timezone(datetime.timedelta(hours = 8))
        return self.e_time - datetime.datetime.now(tzinfo)

    def __str__(self):
        return self.name