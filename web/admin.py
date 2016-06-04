from django.contrib import admin
from web.models import *
# Register your models here.
class UrlRequestAdmin(admin.ModelAdmin):
    pass
admin.register(UrlRequest)
