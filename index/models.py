# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class add_to_db(models.Model):
	add_to_db_text = models.CharField(max_length=100)
	def __unicode__(self):
		return self.add_to_db_text
	def __str__(self):
		return self.add_to_db_text
	class Meta:
		verbose_name = u'note'
		verbose_name_plural = u'notes'


class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name='UserProfile', unique=True)
	avatar = models.ImageField(upload_to='user_avatars/')
	middle_name = models.CharField(max_length=50, blank = True, null=True)

	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], blank=True) # validators should be a list
	
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
