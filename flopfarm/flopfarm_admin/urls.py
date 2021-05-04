'''
Author: your name
Date: 2021-04-29 21:33:43
LastEditTime: 2021-05-04 12:52:25
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /FlopFarmAdminLTE/flopfarm/flopfarm_admin/urls.py
'''

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('market/', views.market, name = 'market'),
    path('purchased/', views.purchased, name = 'purchased'),
    path('market/<uuid:pk>/buy/', views.buy, name = 'buy'),
    path('idle_instance/upload/', views.upload.as_view(), name = 'upload'),
    path('running_instance/', views.running_instance, name = 'running_instance'),
    path('idle_instance/', views.idle_instance, name = 'idle_instance'),
]