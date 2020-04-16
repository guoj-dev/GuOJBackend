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
import dj_rest_auth.registration.urls
from django.contrib import admin
from rest_framework import routers
from django.urls import include, path, re_path
from API.views import *
from . import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from allauth.account.views import confirm_email
from dj_rest_auth.views import (
    LoginView, LogoutView, PasswordChangeView, UserDetailsView)


admin.site.site_header = 'GuOJ 后台管理'

routers = routers.DefaultRouter()
routers.register('users', UserViewSet, basename='user')
routers.register('problemsets', ProblemSetViewSet, basename='problemset')
routers.register('problems', ProblemViewSet, basename='problem')
routers.register('notice', NoticeViewSet, basename='notice')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(routers.urls)),
    re_path(r'^api/auth/login/$', LoginView.as_view(), name='rest_login'),
    # URLs that require a user to be logged in with a valid session / token.
    re_path(r'^api/auth/logout/$', LogoutView.as_view(), name='rest_logout'),
    re_path(r'^api/auth/user/$', UserDetailsView.as_view(),
            name='rest_user_details'),
    re_path(r'^api/auth/password/change/$', PasswordChangeView.as_view(),
            name='rest_password_change'),
    re_path(r'^api/auth/password/reset/',
            include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
]

urlpatterns += staticfiles_urlpatterns()
