# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin


from index import models
# Register your models here.

class group_admin(admin.ModelAdmin):
	list_display = (u'name',u'descript')

class doc_admin(admin.ModelAdmin):
	list_display = (u'name',u'descript')

class userAdmin(admin.ModelAdmin):
	list_display = (u'user', )

admin.site.register(models.group, group_admin)
admin.site.register(models.doc, doc_admin)
admin.site.register(models.UserProfile, userAdmin)
