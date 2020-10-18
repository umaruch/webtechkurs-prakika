from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'qa.views.test', name='home'),
    url(r'^login/', 'qa.views.test'),
    url(r'^signup', 'qa.views.test'),
    url(r'^question/(?P<id>\d+)', 'qa.views.test', name='question'),
    url(r'^ask/', 'qa.views.test', name='ask'),
    url(r'^popular/', 'qa.views.test', name='popular'),
    url(r'^new', 'qa.views.test'),
    url(r'^answer/$', 'qa.views.test', name='answer'),
)
