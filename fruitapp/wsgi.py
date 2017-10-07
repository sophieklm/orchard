"""
WSGI config for fruitapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fruitapp.settings")

application = get_wsgi_application()

# import os
# import sys

# path = os.path.expanduser('~/orchard')
# if path not in sys.path:
#     sys.path.append(path)

# os.environ['DJANGO_SETTINGS_MODULE'] = 'fruitapp.settings'

# from django.core.wsgi import get_wsgi_application
# from django.contrib.staticfiles.handlers import StaticFilesHandler
# application = StaticFilesHandler(get_wsgi_application())
