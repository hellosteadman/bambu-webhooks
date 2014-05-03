from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()
urlpatterns = patterns('',
    url(r'^', include('testproject.myapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^webhooks/', include('bambu_webhooks.urls')),
)

if settings.DEBUG:
	from django.contrib.staticfiles.urls import staticfiles_urlpatterns
	urlpatterns += staticfiles_urlpatterns()