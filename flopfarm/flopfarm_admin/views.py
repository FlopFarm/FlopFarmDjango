'''
Author: your name
Date: 2021-04-29 21:25:00
LastEditTime: 2021-05-04 17:33:56
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /FlopFarmAdminLTE/flopfarm/flopfarm_admin/views.py
'''
from django.shortcuts import render

# Create your views here.
from .models import Instance, ETHaddress
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import BuyInstanceForm

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


@login_required
def dashboard(request):
    instance = Instance.objects.filter(status = 'i')
    
    context = {
        'instance' : instance
    }

    address = ETHaddress.objects.filter(user = request.user)
    context['address'] = address[0].address

    return render(request, 'dashboard.html', context=context)

@login_required
def market(request):
    instance = Instance.objects.filter(status = 'i')
    
    context = {
        'instance' : instance
    }

    address = ETHaddress.objects.filter(user = request.user)
    context['address'] = address[0].address
    
    return render(request, 'market.html', context=context)

@login_required
def purchased(request):
    instance = Instance.objects.filter(user = request.user)
    
    context = {
        'instance' : instance
    }

    address = ETHaddress.objects.filter(user = request.user)
    context['address'] = address[0].address

    return render(request, 'purchased.html', context=context)

@login_required
def running_instance(request):
    instance = Instance.objects.filter(status = 'i')
    
    context = {
        'instance' : instance
    }

    address = ETHaddress.objects.filter(user = request.user)
    context['address'] = address[0].address

    return render(request, 'running_instance.html', context=context)

@login_required
def idle_instance(request):
    instance = Instance.objects.filter(status = 'i')
    
    context = {
        'instance' : instance
    }

    address = ETHaddress.objects.filter(user = request.user)
    context['address'] = address[0].address

    return render(request, 'idle_instance.html', context=context)

import datetime

@login_required
def buy(request, pk):
    instance = get_object_or_404(Instance, pk=pk)

    if request.method == 'POST' :
        
        form = BuyInstanceForm(request.POST, user = request.user, instance = instance)

        if form.is_valid():
            instance.user = request.user
            instance.status = 'r'
            instance.s_time = datetime.datetime.now()
            instance.e_time = datetime.datetime.now() + datetime.timedelta(hours = form.cleaned_data['expect_time'])
            instance.save()
            return HttpResponseRedirect(reverse('purchased'))
    
    else:

        form = BuyInstanceForm(initial = {'expect_time' : 0})

    context = {
        'form' : form,
        'instance' : instance,
    }

    address = ETHaddress.objects.filter(user = request.user)
    context['address'] = address[0].address

    return render(request, 'buy.html', context = context)

from django import http

class upload(CreateView):
    model = Instance
    fields = ['type', 'name', 'OS', 'CPU', 'GPU', 'RAM', 'hourly_price', 'IP', 'username', 'password', 'APIinfo', 'API_price', 'remarks']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.provider = self.request.user
        obj.save()     
        return http.HttpResponseRedirect(reverse('idle_instance'))
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['address'] = (ETHaddress.objects.filter(user = self.request.user))[0].address
        return context


