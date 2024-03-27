# production.py

from .base import *

DEBUG = True

# Update the ALLOWED_HOSTS list with your production domain or IP address
ALLOWED_HOSTS = ['rootedgardendesign.com']

# Configure your production database (e.g., PostgreSQL, MySQL)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'rooted',
#         'USER': 'johnyg',
#         'PASSWORD': 'Compaq15',
#         'HOST': 'localhost',  # Set to your database server's hostname or IP
#         'PORT': '',           # Leave empty to use the default database port
#     }
# }

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/dbname',
        # for django-redis < 3.8.0, use:
        # 'LOCATION': '127.0.0.1:6379',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# Static and media file settings
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Path to collected static files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Other production-specific settings go here

# Load sensitive configuration from environment variables
# DJANGO_SECRET_KEY should be set as an environment variable on your server
# Other sensitive information (e.g., database credentials) should also be loaded this way
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')