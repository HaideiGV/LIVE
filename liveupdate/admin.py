from django.contrib import admin
from liveupdate.models import Update, Contacts, Links, Category, LinkRateEvent


admin.site.register(Update)
admin.site.register(Contacts)
admin.site.register(Links)
admin.site.register(Category)
admin.site.register(LinkRateEvent)