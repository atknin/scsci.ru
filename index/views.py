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

from index.alex_functuins import bot1
from index.updateGalary import updateGalary



def about(request):
	argv = {}
	argv['commands'] = index_models.UserProfile.objects.all()
	argv['commands_len'] = len(index_models.UserProfile.objects.all())
	return render(
	 	request, 'about.html', argv
	 	)

def gallery(request):
	argv = {}
	argv['gallary'] = index_models.Gallary.objects.all().order_by('-id')
	return render(
	 	request, 'gallery.html', argv
	 	)


def index(request):
	argv = {}
	argv['commands_len'] = len(index_models.UserProfile.objects.all())
	argv['carousel'] = index_models.coursel_index_page.objects.last()
	#-----------------------ALEX------------------
	newid = bot1()
	if newid != False:
		newid = list(newid)
		h = 0
		for i in newid[0]:
			a = index_models.botnews1.objects.create(news=newid[1][h],news_id=newid[0][h],news_date=newid[2][h],news_pic=newid[3][h][0],news_pic1=newid[3][h][1],news_pic2=newid[3][h][2],news_pic3=newid[3][h][3],news_pic4=newid[3][h][4])# news_author=newid[3][h],news_pic=newid[4][h])
			a.save()
			h = h + 1
	#-----------------------ALEX------------------

	argv['news'] = index_models.botnews1.objects.all().order_by('-id')[:3]
	try:
		getpost = requests.get(url='https://api.telegram.org/bot358613549:AAHmzux6VX3_D8RVMpl1WIb5fxxpN_i8tJE/getUpdates').json()
		mes = getpost['result'][-1]['message']['text']
		if mes != 'none':
			argv['sos_message'] = mes
	except Exception as e:
		pass
	updateGalary()
	argv['gallary'] = index_models.Gallary.objects.all().order_by('-id')[:12]
	return render(request, 'index.html', argv)

@csrf_exempt
def add_to_db(request):
	if request.method == "POST":
		a = index_models.add_to_db.objects.create(add_to_db_text=request.POST['message'])
		a.save()
	argv = {}
	argv['mes'] = index_models.add_to_db.objects.all()
	return render(request, 'add_to_db.html',argv)
