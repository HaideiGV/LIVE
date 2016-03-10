from django.contrib import admin
from liveupdate.models import Update, ViewAllTypeFields, Links, Category


admin.site.register(Update)
admin.site.register(ViewAllTypeFields)
admin.site.register(Links)
admin.site.register(Category)