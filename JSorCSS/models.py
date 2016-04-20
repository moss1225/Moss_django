from __future__ import unicode_literals

from django.db import models
from django.http.response import HttpResponse
import time
from django.shortcuts import render

# Create your models here.

def JS_View(request):
    response = 'form JSorCSS'
    return HttpResponse("<p style='width:100%;text-align:center;color:orange;'>" + response + "</p>")

def CSS_View(request):
    context = {}
    return render(request, 'test_js_css.html', context)
