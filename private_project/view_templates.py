# -*- coding: utf-8 -*-

#from django.http import HttpResponse
from django.shortcuts import render

def temp1(request):
    context = {}
    return render(request, 'templates-1.html', context)

def temp2(request):
    context = {}
    return render(request, 'templates-2.html', context)
