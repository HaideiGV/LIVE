from django.conf.urls import *
import liveupdate.views


urlpatterns = patterns(
    '',
    (r'^$', liveupdate.views.allLinksPage),
    (r'^send-form/$', liveupdate.views.all_type_input_form),
    (r'^add-link/$', liveupdate.views.new_link),
    (r'^about/$', liveupdate.views.about),
    (r'^ajax_result/$', liveupdate.views.ajax_result),
    (r'^accounts/login/$', liveupdate.views.login),
    url(r'^like/$', liveupdate.views.likes, name='like'),
    )
