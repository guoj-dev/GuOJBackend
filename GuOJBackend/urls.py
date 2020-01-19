"""GuOJBackend URL Configuration

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
from django.contrib import admin
from rest_framework import routers
from django.urls import include, path
from API.views import *
from . import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import xadmin

admin.site.site_header='GuOJ 后台管理'

import rest_auth.registration.urls
routers=routers.DefaultRouter()
routers.register('users',UserViewSet,basename='user')
routers.register('problemsets',ProblemSetViewSet,basename='problemset')
routers.register('problems',ProblemViewSet,basename='problem')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('api/', include(routers.urls)),
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),
]

urlpatterns += staticfiles_urlpatterns()