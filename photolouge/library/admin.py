# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from library.models import Photo


class PhotoAdmin(admin.ModelAdmin):
    pass
    # list_display = ('id', 'name', 'archive')
    # list_editable = ('archive', )
    # list_filter = ('archive', )
    # search_fields = ('name',)
    # prepopulated_fields = {"slug": ("name",)}


admin.site.register(Photo, PhotoAdmin)


