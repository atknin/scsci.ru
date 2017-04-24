# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin


from index import models
# Register your models here.


class userAdmin(admin.ModelAdmin):
	list_display = (u'user', )

class userfiles(admin.ModelAdmin):
	list_display = ('name', u'short_description' )

admin.site.register(models.UserProfile, userAdmin)
admin.site.register(models.user_files, userfiles)
