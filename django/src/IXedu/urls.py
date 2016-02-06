"""IXedu URL Configuration

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
from uni.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', 'uni.views.home',name='home'),
    url(r'^create_uni/$', 'uni.views.create_uni',name='create_uni'),
    url(r'^university_page/$', 'uni.views.university_page',name='university_page'),
    url(r'^login/$', 'django.contrib.auth.views.login',name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout',name="logout"),

    url(r'^create_univ/$', CreateUniv.as_view()),

    url(r'^$','uni.views.home',name='home'),
    url(r'^search$', SearchPage.as_view()),
    url(r'^policyform$', PolicyForm.as_view()),

]
