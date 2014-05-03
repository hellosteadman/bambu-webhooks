from django.conf.urls import patterns, url
from django.conf import settings
from bambu_webhooks.views import webhooks

if 'bambu_bootstrap' in settings.INSTALLED_APPS:
    from bambu_bootstrap.decorators import body_classes
else:
    def body_classes(view, *classes):
        return view

urlpatterns = patterns('',
    url(r'^$', body_classes(webhooks, 'profile', 'profile-edit', 'webhooks'), name = 'webhooks_manage'),
)