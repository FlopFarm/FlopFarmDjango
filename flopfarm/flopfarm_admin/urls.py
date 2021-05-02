'''
Author: your name
Date: 2021-04-29 21:33:43
LastEditTime: 2021-05-02 15:57:41
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /FlopFarmAdminLTE/flopfarm/flopfarm_admin/urls.py
'''

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('market/', views.market, name = 'market')
]