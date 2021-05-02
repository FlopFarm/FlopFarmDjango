'''
Author: your name
Date: 2021-04-29 21:33:43
LastEditTime: 2021-05-01 23:33:31
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /FlopFarmAdminLTE/flopfarm/flopfarm_admin/urls.py
'''

from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('market/', views.market, name = 'market')
]