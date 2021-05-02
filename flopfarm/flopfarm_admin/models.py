'''
Author: your name
Date: 2021-04-29 21:25:00
LastEditTime: 2021-05-02 14:14:40
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /FlopFarmAdminLTE/flopfarm/flopfarm_admin/models.py
'''
from django.db import models
import uuid

# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular user')
    username = models.CharField(max_length=200, help_text='Enter the user name')
    password = models.CharField(max_length=200, help_text='Enter the password')

    def __str__(self):
        return f'{self.username} ({self.id})'

class EdgeProvider(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular user')
    username = models.CharField(max_length=200, help_text='Enter the user name')
    password = models.CharField(max_length=200, help_text='Enter the password')

    def __str__(self):
        return f'{self.username} ({self.id})'

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
        default = 'o', 
        help_text='Instance status'
    )

    OS = models.CharField(max_length=200, blank = True, null = True, help_text='Enter the Operating System info')
    CPU = models.CharField(max_length=200, blank = True, null = True, help_text='Enter the CPU info')
    GPU = models.CharField(max_length=200, blank = True, null = True, help_text='Enter the GPU info')
    RAM = models.CharField(max_length=200, blank = True, null = True, help_text='Enter the RAM info')
    hourly_price = models.FloatField(blank = True, null = True, help_text='Enter the hourly price')

    APIinfo = models.CharField(max_length=200,blank = True, null = True, help_text='Enter the API info')
    API_price = models.FloatField(blank = True, null = True, help_text='Enter the price per use for API')

    remarks = models.CharField(max_length=200, blank = True, null = True, help_text='Enter the remarks')

    provider = models.ForeignKey('EdgeProvider', on_delete=models.SET_NULL, null=True, related_name='Instance_provided')
    user = models.ForeignKey('User', on_delete=models.SET_NULL, blank = True, null=True, related_name='Instance_using')

    def __str__(self):
        return self.name