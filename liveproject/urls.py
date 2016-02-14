from django.contrib import admin
from django.conf.urls import *
from liveupdate.models import Update
from liveupdate.views import update,scripts
import liveupdate.views


urlpatterns = patterns(
    '',
    url(r'^update/$', update),
    url(r'^admin/', include(admin.site.urls)),
    (r'^scripts/([^/]+)$', scripts),
    (r'^updates-after/(?P<id>\d+)/$', liveupdate.views.updates_after),
    (r'^send_message/$', liveupdate.views.type_post),
    )
