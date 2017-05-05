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
		verbose_name = u'Срочное сообщение'
		verbose_name_plural = u'Срочны сообщение'


class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name='UserProfile', unique=True)
	avatar = models.ImageField(upload_to='user_avatars/', blank = True)
	middle_name = models.CharField(max_length=50, blank = True, null=True)

	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True) # validators should be a list

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


class coursel_photos(models.Model):
	head = models.CharField(max_length=30)
	short_description = models.CharField(max_length=100,blank = True, null=True)
	picture = models.ImageField(upload_to='coursel_picture/', blank = True)

	class Meta:
		verbose_name = u'фото для карусели'
		verbose_name_plural = u'фотографии для карусели'

	def __unicode__(self):
		return self.head
	def __str__(self):
		return self.head

class coursel_index_page(models.Model):
	text = models.CharField(max_length=600)
	photos = models.ManyToManyField(coursel_photos)

	class Meta:
		verbose_name = u'Карусель слайд на главной'
		verbose_name_plural = u'Карусель слайды на главной'

	def __unicode__(self):
		return self.text
	def __str__(self):
		return self.text

class botnews1(models.Model):
	news = models.CharField(max_length=10000)
	news_id = models.CharField(max_length=1000)
	news_date = models.CharField(max_length=1000)
	def __unicode__(self):
		return self.news
	def __str__(self):
		return self.news
	class Meta:
		verbose_name = u'новость'
		verbose_name_plural = u'новости'

class Gallary(models.Model):
	photo_big = models.ImageField(upload_to='gallary/big/', blank = True)
	photo_small = models.ImageField(upload_to='gallary/small/', blank = True)
	photo_id = models.IntegerField(unique=True)

	class Meta:
		verbose_name = u'фото в Галерею'
		verbose_name_plural = u'фотки Галереи'

	def __unicode__(self):
		return str(self.photo_id)
	def __str__(self):
		return str(self.photo_id)
