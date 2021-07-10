"""Wira_Proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from typing import Pattern
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.urls.resolvers import URLPattern
from Users import views as User_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',User_views.register, name="Register"),
    path('login/',auth_views.LoginView.as_view(template_name = 'Users/login.html'),name='Login'),
    path('profile/', User_views.Profile, name="Profile_Page"),
    path('',include('Job.urls'))
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, Document_root = settings.MEDIA_ROOT)