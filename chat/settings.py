# webchat_project/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chat',  # Nova app
]

# Configuració de zona horària
LANGUAGE_CODE = 'ca'
TIME_ZONE = 'Europe/Madrid'
USE_TZ = True

# Configuració d'arxius estàtics
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# Configuració de sessió
SESSION_COOKIE_AGE = 86400  # 24 hores