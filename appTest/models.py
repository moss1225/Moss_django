from __future__ import unicode_literals

from django.db import models
from django.http.response import HttpResponse
import time

# Create your models here.

def appView(request):
    now = time.strftime("%Y-%m-%d %X", time.localtime())
    response = "now is: " + now
    #print response
    return HttpResponse("<p style='width:100%;text-align:center;color:orange;'>" + response + "</p>")

