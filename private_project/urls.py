"""private_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from private_project.view_index import hello
from private_project.view_cafe import cafe
from private_project.view_templates import temp1, temp2
import appTest.models 
import settings
import JSorCSS
urlpatterns = [
    url(r"^$", hello),
    url(r'^cafe/', cafe),
    url(r'^temp1/', temp1),
    url(r'^temp2/', temp2),
    url(r'^clock/', appTest.models.appView),
    url(r'^js/', JSorCSS.models.JS_View),
    url(r'^css/',JSorCSS.models.CSS_View),
    url(r'^admin/', admin.site.urls),
    url( r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': settings.STATIC_URL }),
]
