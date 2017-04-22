# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from django.contrib import auth
from index import models as index_models
from index.email_module import sendEmail

def add_to_group(request, pk):
	arg = {}
	user = User.objects.get(id=pk)
	group = Group.objects.get(name='Users')
	if not user.groups.filter(name = 'Users').exists():
		group.user_set.add(user)
		text = user.first_name+', Вы добавлены в базу данных пользователей страницей кооператва "солнечный остров"'
		link = 'sostrov.com'
		arg['status'] = user.first_name + ' ' + user.last_name + '('+ user.email+ ')' + 'успешно добавлен в пользователи сайтом.'
		try:
			sendEmail(link,text,user.email,'koop.sostrov@gmail.com','soostrov')
		except:
			arg['status']+=' Внимание: Пользователь не был уведомлен о его успешном добавлени на сайт, система не email отправить письмо.'
	else:
		arg['status'] = 'Пользователь уже добавлен. '
	return render(
	 	request, 'added.html', arg
	 	)

def index(request):
 	return render(
	 	request, 'index.html',
	 	)
