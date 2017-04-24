# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
	user   = models.OneToOneField(User, unique=True)
	avatar = models.ImageField(upload_to='user_avatars/')
	paper_title = models.CharField(max_length=200,blank = True, null=True)
	paper_short_description = models.CharField(max_length=800,blank = True, null=True)
	birth_day = models.DateField(blank = True, null = True)

	def __unicode__(self):
		return u'{c}/{l}'.format(c=self.user.first_name, l=self.last_name)

	def __str__(self):
		return self.user.username
	class Meta:
		verbose_name = 'User'
		verbose_name_plural = u'Users'

class user_files(models.Model):
	name = models.CharField(max_length=30)
	short_description = models.CharField(max_length=200,blank = True, null=True)
	user_file = models.FileField(upload_to='user_files/')
	user = models.ManyToManyField(UserProfile,related_name='user_files')


	class Meta:
		verbose_name = u'Файл'
		verbose_name_plural = u'Файлы'

	def __unicode__(self):
		return u'{c}/{l}'.format(c=self.name, l=self.short_description)

	def __str__(self):
		return self.name
