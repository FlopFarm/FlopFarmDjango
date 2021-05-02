'''
Author: your name
Date: 2021-04-29 21:25:00
LastEditTime: 2021-05-02 00:01:35
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /FlopFarmAdminLTE/flopfarm/flopfarm_admin/views.py
'''
from django.shortcuts import render

# Create your views here.
from .models import User, Instance, EdgeProvider

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

def market(request):
    instance = Instance.objects.all()
    
    context = {
        'instance' : instance
    }
    
    return render(request, 'market.html', context=context)
    