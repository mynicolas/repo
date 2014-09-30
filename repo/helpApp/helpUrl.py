#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from views import getHelpContent

urlpatterns = patterns('',
    url(r'^$', getHelpContent),
)