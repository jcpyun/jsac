"""
WSGI config for detl project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "IXedu.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


try:
	from dj_static import Cling

	application = Cling(get_wsgi_application())
except:
	pass
	