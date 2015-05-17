from django.contrib import admin
from django.conf.urls import *
from liveupdate.models import Update
from liveupdate.views import update


urlpatterns = patterns(
    '',
    #'django.views.generic',
    #url(r'^$', 'list_default.object_list', {'queryset': Update.objects.all()}),
    #url(r'^$', 'django.views.generic', {'queryset': Update.objects.all()}),
    url(r'^update/$', update),
    url(r'^admin/', include(admin.site.urls)),
    )
