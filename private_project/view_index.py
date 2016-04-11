# -*- coding: utf-8 -*-

#from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    context = {}
    context['wx'] = 'please try WeiXin!'
    #传递参数 'wx'
    return render(request, 'index.html', context)
    #返回页面'index.html',并传递参数'wx',html通过{{wx}}接受