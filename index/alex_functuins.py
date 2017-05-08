import vk
import time
from index import models
from index.passwords import pass_vk

def bot1():
	session = vk.AuthSession('5943322', '+79151322437', 'pass_vk', scope='wall, messages')
	vk_api = vk.API(session)

	new = {}

	new['test'] = models.botnews1.objects.all()
	new1 = vk_api.wall.get(domain='testbotmyag')

	ids = True

	for h in reversed(new['test']):
		if str(new1[1]['id']) == h.news_id:
			ids = False
		break


	t = 0
	l = 1
	nameid = {}
	name = {}
	k = 0
	hy = {}
	ifyes = {}
	ifyestext = {}
	ifyesdate = {}
	ifyesname = {}
	ifyesname = {}
	ifyespic = {}

	if ids != False:
		for i in new['test']:
			hy[k] = i.news_id
			k = k + 1
		NO = {}
		p = k
		can = False
		if new1[0] != 0:
			if k != 0:
				for i in new['test']:
					k1 = 0
					l = new1[0]
					while k1 != new1[0]:
						if hy[k-p] != str(new1[l]['id']):
							ifyes[k1] = new1[l]['id']
							ifyestext[k1] = new1[l]['text']
							ifyesdate[k1] = time.strftime("%d %b %Y", time.localtime(new1[l]['date']))
							# nameid[k1] = vk_api.users.get(user_ids=new1[l]['from_id'])
							# name[k1] = nameid[k1][0]['first_name'] + ' ' + nameid[k1][0]['last_name']
							# ifyesname[k1] = name[k1]
							ifyespic[k1] = {}
							k2 = 0
							if 'attachments' in new1[l]:
								for i in new1[l]['attachments']:
									ifyespic[k1][k2] = i['photo']['src']
									k2 = k2 + 1
								if k2 != 5: #Кол-во картинок
									while k2 != 5: #Кол-во картинок
										ifyespic[k1][k2] = ''
										k2 = k2 + 1
								can = True
							else:
								k2 = 0
								while k2 != 5: #Кол-во картинок
									ifyespic[k1][k2] = ''
									k2 = k2 + 1
								can = True
						else:
							NO[k1] = new1[l]['id']
						l = l - 1
						k1 = k1 + 1
					p = p - 1
			else:
				k1 = 0
				l = new1[0]
				while k1 != new1[0]:
					ifyes[k1] = new1[l]['id']
					ifyestext[k1] = new1[l]['text']
					ifyesdate[k1] = time.strftime("%d %b %Y", time.localtime(new1[l]['date']))
					# nameid[k1] = vk_api.users.get(user_ids=new1[l]['from_id'])
					# name[k1] = nameid[k1][0]['first_name'] + ' ' + nameid[k1][0]['last_name']
					# ifyesname[k1] = name[k1]
					ifyespic[k1] = {}
					k2 = 0
					if 'attachments' in new1[l]:
						for i in new1[l]['attachments']:
							ifyespic[k1][k2] = i['photo']['src']
							k2 = k2 + 1
						if k2 != 5: #Кол-во картинок
							while k2 != 5: #Кол-во картинок
								ifyespic[k1][k2] = ''
								k2 = k2 + 1
						can = True
					else:
						k2 = 0
						while k2 != 5: #Кол-во картинок
							ifyespic[k1][k2] = ''
							k2 = k2 + 1
						can = True
					l = l - 1
					k1 = k1 + 1

			for u in NO:
				if u in ifyes:
					del ifyes[u]
				if u in ifyestext:
					del ifyestext[u]
				if u in ifyesdate:
					del ifyesdate[u]
				if u in ifyesname:
					del ifyesname[u]
				if can == True:
					if u in ifyespic:
						del ifyespic[u]
			ifyes = list(ifyes.values())
			ifyestext = list(ifyestext.values())
			ifyesdate = list(ifyesdate.values())
			ifyesname = list(ifyesname.values())
			if can == True:
				for i in ifyespic:
					ifyespic[i] = list(ifyespic[i].values())
				ifyespic = list(ifyespic.values())
			if can == False:
				return(ifyes, ifyestext, ifyesdate)#, ifyesname)
			else:
				return(ifyes, ifyestext, ifyesdate, ifyespic)#ifyesname, ifyespic)
		else:
			return(False)
	else:
		return(False)
