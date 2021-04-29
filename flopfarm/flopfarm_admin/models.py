'''
Author: your name
Date: 2021-04-29 21:25:00
LastEditTime: 2021-04-29 22:11:02
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
        return f'{self.id} ({self.username})'

class Instance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular instance')
    name = models.CharField(max_length=200, help_text='Enter the instance name')
    
    TYPE = (
        ('c', 'General Computing Instance'),
        ('d', 'Deep Learning API')
    )

    STATUS = (
        ('a', 'Available'),
        ('u', 'Serving'),
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
        help_text='Instance type'
    )
    
    # provider = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, related_name='Instance_provided')
    # user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, related_name='Instance_using')

    def __str__(self):
        return self.name