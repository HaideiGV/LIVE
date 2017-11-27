from django.conf.urls import *
import liveupdate.views
from liveupdate.views import UserView
from django.contrib import admin

urlpatterns = patterns(
    '',
    (r'^$', liveupdate.views.all_links),
    (r'^add-link/$', liveupdate.views.new_link),
    (r'^about/$', liveupdate.views.about),
    (r'^send-form/$', liveupdate.views.contact_form),
    url(r'^register/$', UserView.as_view(), name='register'),
    (r'^register_success/$', liveupdate.views.register_success),
    (r'^rating_filter/$', liveupdate.views.filter_rate),
    (r'^login/$', liveupdate.views.login_page),
    (r'^logout/$', liveupdate.views.logout_page),
    (r'^accounts/login/$', liveupdate.views.login_page),
    url(r'^like/$', liveupdate.views.likes, name='like'),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'', include('social_auth.urls')),
    url(r'^home/$', liveupdate.views.home, name='home'),
    # url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),

    )
