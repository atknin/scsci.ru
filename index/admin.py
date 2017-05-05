# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin


from index import models
# Register your models here.


class userAdmin(admin.ModelAdmin):
	list_display = (u'user', u'profile_username')
	def profile_username(self, obj):
		return obj.user.last_name + ' ' +  obj.user.first_name
	profile_username.short_description = 'FI'

class userfiles(admin.ModelAdmin):
	list_display = (u'name', u'short_description' )

class add_to_db_admin(admin.ModelAdmin):
	list_display = (u'add_to_db_text', )

class coursel_index_page_admin(admin.ModelAdmin):
	list_display = (u'text',)

class coursel_photos_admin(admin.ModelAdmin):
	list_display = (u'head', u'short_description')

class Gallary_admin(admin.ModelAdmin):
	list_display = (u'photo_id', )

admin.site.register(models.UserProfile, userAdmin)
admin.site.register(models.user_files, userfiles)
admin.site.register(models.add_to_db, add_to_db_admin)
admin.site.register(models.coursel_index_page, coursel_index_page_admin)
admin.site.register(models.coursel_photos, coursel_photos_admin)
admin.site.register(models.Gallary, Gallary_admin)
