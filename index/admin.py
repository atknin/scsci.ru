# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin


from index import models
# Register your models here.


class userAdmin(admin.ModelAdmin):
	list_display = (u'user', )

class userfiles(admin.ModelAdmin):
	list_display = (u'name', u'short_description' )

class add_to_db_admin(admin.ModelAdmin):
	list_display = (u'add_to_db_text', )

admin.site.register(models.UserProfile, userAdmin)
admin.site.register(models.user_files, userfiles)
admin.site.register(models.add_to_db, add_to_db_admin)
