'''
Author: your name
Date: 2021-04-29 21:25:00
LastEditTime: 2021-04-30 01:25:27
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /FlopFarmAdminLTE/flopfarm/flopfarm_admin/views.py
'''
from django.shortcuts import render

# Create your views here.
from flopfarm_admin.models import User, Instance

def login(request):
    """View function for home page of site."""
    context = {
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'login.html', context=context)

def dashboard(request):
    context = {

    }

    return render(request, 'dashboard.html', context=context)