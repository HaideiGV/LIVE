from django.contrib import admin
from django.conf.urls import *
from liveupdate.views import update, scripts
import liveupdate.views
from liveupdate.views import allView


urlpatterns = patterns(
    '',
    url(r'^detail/$', update),
    url(r'^admin/', include(admin.site.urls)),
    (r'^scripts/([^/]+)$', scripts),
    (r'^updates-after/(?P<id>\d+)/$', liveupdate.views.updates_after),
    (r'^links/$', liveupdate.views.allLinksPage),
    # (r'^links/$', liveupdate.views.ajax_update),
    (r'^links/$', liveupdate.views.updateRate),
    (r'^all$', allView.as_view()),
    (r'^send-form/$', liveupdate.views.all_type_input_form),
    (r'^$', liveupdate.views.new_link),
    (r'^login/$', liveupdate.views.login_page),
    )
