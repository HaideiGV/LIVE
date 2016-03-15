from django.contrib import admin
from django.conf.urls import *
from liveupdate.views import update
import liveupdate.views
from liveupdate.views import allView


urlpatterns = patterns(
    '',
    url(r'^detail/$', update),
    url(r'^admin/', include(admin.site.urls)),
    (r'^updates-after/(?P<id>\d+)/$', liveupdate.views.updates_after),
    (r'^$', liveupdate.views.allLinksPage),
    (r'^send-form/$', liveupdate.views.all_type_input_form),
    (r'^add-link/$', liveupdate.views.new_link),
    (r'^about/$', liveupdate.views.about),
    (r'^login/$', liveupdate.views.login_page),
    )
