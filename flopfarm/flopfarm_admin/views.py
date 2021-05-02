'''
Author: your name
Date: 2021-04-29 21:25:00
LastEditTime: 2021-05-02 19:32:03
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /FlopFarmAdminLTE/flopfarm/flopfarm_admin/views.py
'''
from django.shortcuts import render

# Create your views here.
from .models import Instance
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import BuyInstanceForm

@login_required
def dashboard(request):
    context = {

    }

    return render(request, 'dashboard.html', context=context)

@login_required
def market(request):
    instance = Instance.objects.all()
    
    context = {
        'instance' : instance
    }
    
    return render(request, 'market.html', context=context)

@login_required
def purchased(request):
    context = {

    }

    return render(request, 'purchased.html', context=context)

@login_required
def running_instance(request):
    context = {

    }

    return render(request, 'running_instance.html', context=context)

@login_required
def idle_instance(request):
    context = {

    }

    return render(request, 'idle_instance.html', context=context)

@login_required
def buy(request, pk):
    instance = get_object_or_404(Instance, pk=pk)

    if request.method == 'POST' :
        
        form = BuyInstanceForm(request.POST, user = request.user, instance = instance)

        if form.is_valid():
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect(reverse('purchased'))
    
    else:

        form = BuyInstanceForm(initial = {'expect_time' : 0})

    context = {
        'form' : form,
        'instance' : instance,
    }

    return render(request, 'buy.html', context = context)


