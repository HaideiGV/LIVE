from django.conf.urls import *
import liveupdate.views
from liveupdate.views import UserView


urlpatterns = patterns(
    '',
    (r'^$', liveupdate.views.allLinksPage),
    (r'^send-form/$', liveupdate.views.all_type_input_form),
    (r'^add-link/$', liveupdate.views.new_link),
    (r'^about/$', liveupdate.views.about),
    url(r'^register/$', UserView.as_view(), name='register'),
    (r'^register_success/$', liveupdate.views.register_success),
    (r'^ajax_result/$', liveupdate.views.ajax_result),
    (r'^login/$', liveupdate.views.login_page),
    (r'^logout/$', liveupdate.views.logout_page),
    (r'^accounts/login/$', liveupdate.views.login_page),
    url(r'^like/$', liveupdate.views.likes, name='like'),
    )
