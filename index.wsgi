#import sae
#from repo import wsgi

#application = sae.create_wsgi_app(wsgi.application)

import os
import sys

apache_configuration = os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)
sys.path.append(workspace)
sys.path.append("/var/www/html/repo")
sys.path.append("/var/www/html/repo/repo")

os.environ['DJANGO_SETTINGS_MODULE'] = 'repo.settings'
os.environ['PYTHON_EGG_CACHE'] = '/tmp'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
