# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from django.contrib import auth
from index import models as index_models
from index.email_module import sendEmail

def about(request):
	argv = {}
	argv['commands'] = index_models.UserProfile.objects.all()
	argv['commands_len'] = len(index_models.UserProfile.objects.all())
	return render(
	 	request, 'about.html', argv
	 	)

def index(request):
	argv = {}
	argv['commands_len'] = len(index_models.UserProfile.objects.all())

	return render(request, 'index.html',argv)
