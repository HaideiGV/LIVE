from django.contrib import admin
from django.conf.urls import *
from liveupdate.models import Update


urlpatterns = patterns('',
    #'django.views.generic',
    #url(r'^$', 'list_default.object_list', {'queryset': Update.objects.all()}),
    url(r'^admin/', include(admin.site.urls)),
    )
