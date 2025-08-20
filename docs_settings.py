"""
Minimal Django settings for building Sphinx documentation on Read the Docs.
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = 'dummy-key-for-documentation-build-only-not-for-production'
DEBUG = True

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',  # Required for model imports
    'referral',  # Your app - this is what we're documenting!
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',  # Use in-memory database for docs
    }
}

USE_TZ = True
TIME_ZONE = 'UTC'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Disable middleware and other unnecessary components for docs
MIDDLEWARE = []

# Required for Django 4.0+
if os.environ.get('READTHEDOCS') == 'True':
    # Set a more permissive allowed hosts for Read the Docs
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']