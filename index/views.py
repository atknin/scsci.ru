# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from django.contrib import auth
from index import models as index_models
from index.email_module import sendEmail
from django.views.decorators.csrf import csrf_exempt
import requests

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
	argv['carousel'] = index_models.coursel_index_page.objects.last()
	try:
		getpost = requests.get(url='https://api.telegram.org/bot358613549:AAHmzux6VX3_D8RVMpl1WIb5fxxpN_i8tJE/getUpdates').json()
		mes = getpost['result'][-1]['message']['text']
		if mes != 'none':
			argv['sos_message'] = mes
	except Exception as e:
		pass

	return render(request, 'index.html', argv)

@csrf_exempt
def add_to_db(request):
	if request.method == "POST":
		a = index_models.add_to_db.objects.create(add_to_db_text=request.POST['message'])
		a.save()
	argv = {}
	argv['mes'] = index_models.add_to_db.objects.all()
	return render(request, 'add_to_db.html',argv)
