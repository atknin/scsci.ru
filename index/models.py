# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
	user   = models.ForeignKey(User, unique=True)
	avatar = models.ImageField(upload_to='user_avatars/')
	paper_title = models.CharField(max_length=200,blank = True, null=True)
	paper_short_description = models.CharField(max_length=500,blank = True, null=True)

	def __unicode__(self):
		return self.user.username

	def __str__(self):
		return self.user.username
	class Meta:
		verbose_name = 'User'
		verbose_name_plural = u'Users'

class group(models.Model):
	name = models.CharField(max_length=30,blank = True, null=True)
	descript = models.CharField(max_length=200,blank = True, null=True)
	id = models.AutoField(primary_key=True)

	class Meta:
		verbose_name = u'Группа'
		verbose_name_plural = u'Группы'

	def __unicode__(self):
		return self.name.encode('utf-8')

	def __str__(self):
		return self.name

class doc(models.Model):
	name = models.CharField(max_length=70)
	descript = models.CharField(max_length=500, blank = True, null=True)
	# picture =  models.ImageField(upload_to='', blank=True)
	file = models.FileField(upload_to='', blank=True)
	group = models.ForeignKey('group',on_delete=models.CASCADE,default=1, verbose_name = 'группа')

	class Meta:
		verbose_name = u'Документ'
		verbose_name_plural = u'Документы'

	def __unicode__(self):
		return self.name.encode('utf-8')

# class news(models.Model):
# 	name = models.CharField(max_length=70)
# 	descript = models.CharField(max_length=500, blank = True, null=True)
# 	picture =  models.ImageField(upload_to='', blank=True)
# 	file = models.FileField(upload_to='', blank=True)

# 	class Meta:
# 		verbose_name = u'Новость'
# 		verbose_name_plural = u'Новости'

# 	def __unicode__(self):
# 		return self.name.encode('utf-8')
