from django.contrib import admin
from django.conf.urls import *
from liveupdate.models import Update
from liveupdate.views import update,scripts
import liveupdate.views


urlpatterns = patterns(
    '',
    #'django.views.generic',
    #url(r'^$', 'list_default.object_list', {'queryset': Update.objects.all()}),
    #url(r'^$', 'django.views.generic', {'queryset': Update.objects.all()}),
    url(r'^update/$', update),
    url(r'^admin/', include(admin.site.urls)),
    (r'^scripts/([^/]+)$', scripts),
    #(r'^updates-after/(?P<id>\d+)/$',liveupdate.views.updates_after),
    (r'^updates-after/(?P<id>\d+)/$',liveupdate.views.type_post),
    )
