"""
WSGI config for jgdesigns project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jgdesigns.settings.dev")

# application = get_wsgi_application()


import os
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

# Load environment variables from .env file
load_dotenv()

# Set the default Django settings module for the 'wsgi' application.
environment = os.getenv('DJANGO_ENV', 'development')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jgdesigns.settings.{environment}')

# Get the application instance
application = get_wsgi_application()