"""vanthink_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'inputinfo',views.inputInfo,name='inputinfo'),
    path(r'devices',views.show_devices,name='showDevices'),
    path(r'saveinfo', views.saveInfo, name='saveinfo'),
    path(r'^startservices/(?P<e_name>[0-9a-zA-Z]+)/(?P<e_uuid>[0-9a-zA-Z_]+)/(?P<plat_verion>[0-9a-zA-Z]+)/$',views.startservice,name='startserver'),
    path(r'^stopservices/(?P<gid>[0-9a-zA-Z]+)/(?P<e_uuid>[0-9a-zA-Z]+)/$',views.stopservice, name='stopserver'),
    path(r'^showreport/(?P<gid>[0-9a-zA-Z]+)/$', views.showreport, name='showreport'),

]
