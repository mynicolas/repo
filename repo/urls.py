#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *

# from django.contrib import admin
from repo.views import repo_index
from helpApp import helpUrl

urlpatterns = patterns('',
    # (r'^admin', include(admin.site.urls)),
    (r'^$', repo_index),
    (r'^help', include(helpUrl)),
)

