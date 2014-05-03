from os import path

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'database.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': ''
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = path.abspath(path.join(path.dirname(__file__), '../static'))
STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'djangobower.finders.BowerFinder'
)

BOWER_COMPONENTS_ROOT = path.abspath(path.join(path.dirname(__file__), '../bower'))

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'bambu_analytics.middleware.AnalyticsMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.core.context_processors.debug',
	'django.core.context_processors.request',
	'django.contrib.auth.context_processors.auth',
	'django.contrib.messages.context_processors.messages',
	'bambu_bootstrap.context_processors.basics'
)

SITE_ID = 1
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'bambu_bootstrap',
    'bambu_cron',
    'bambu_webhooks',
    'testproject.myapp',
    'djangobower'
)

BOWER_INSTALLED_APPS = (
	'bootstrap',
	'bootstrap-datepicker',
	'fontawesome'
)

SECRET_KEY = 'sm8apo4(o4ni9n=nsn7-3x8g@fkeuckm(#ixpk5lw3vrzq*ads'
ROOT_URLCONF = 'testproject.urls'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

SITE_ROOT = path.abspath(path.dirname(__file__) + '/../')
STATIC_ROOT = path.join(SITE_ROOT, 'static')
TEMPLATE_DIRS = (
    path.join(SITE_ROOT, 'templates'),
)

ANALYTICS_SETTINGS = {
    'UniversalAnalyticsProvider': {
        'ID': 'UA-XXXXXXXX-XX'
    }
}