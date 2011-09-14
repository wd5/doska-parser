from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^list/$', 'core.views.list'),
    url(r'^next/$', 'core.views.next'),
    url(r'^show/(?P<id>\d+)/$', 'core.views.adv_show'),
    url(r'^import/(?P<id>\d+)/$', 'core.views.adv_import'),
    url(r'^delete/(?P<id>\d+)/$', 'core.views.adv_delete'),
    url(r'^wait/(?P<id>\d+)/$', 'core.views.adv_wait'),
    url(r'^mapping/$', 'core.views.mapping')
)