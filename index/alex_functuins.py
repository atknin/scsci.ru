import vk
import time
from index import models
from index.passwords import pass_vk

def bot1():
	session = vk.AuthSession('5943322', '+79151322437', pass_vk, scope='wall, messages')
	vk_api = vk.API(session)
	bot = "scsci"

	new = {}

	new['test'] = models.botnews1.objects.all()
	new1 = vk_api.wall.get(domain=bot)

	k = 0
	hy = {}
	ifyes = {}
	ifyestext = {}
	ifyesdate = {}
	for i in new['test']:
		hy[k] = i.news_id
		print('hy[',k,'] = ',i.news_id)
		k = k + 1
	NO = {}
	p = k

	if new1[0] != 0:
		print('\t all:',new1[0],'ID:',new1[new1[0]]['id'],'K:',k)
		if k != 0:
			for i in new['test']:
				print('\t \t P:',p)
				k1 = 0
				l = new1[0]
				print('\n \t -------  --------  ------- \n')
				while k1 != new1[0]:
					if hy[k-p] != str(new1[l]['id']):
						print('yes')
						ifyes[k1] = new1[l]['id']
						ifyestext[k1] = new1[l]['text']
						ifyesdate[k1] = time.strftime("%d %b %Y", time.localtime(new1[l]['date']))
					else:
						NO[k1] = new1[l]['id']
						print('\t NO:', NO)
					l = l - 1
					k1 = k1 + 1
				p = p - 1
			print('ifyes',ifyes)
		else:
			k1 = 0
			l = new1[0]
			print('\n \t ------- NOTMAIN -------- NOTMAIN ------- \n')
			while k1 != new1[0]:
				ifyes[k1] = new1[l]['id']
				ifyestext[k1] = new1[l]['text']
				ifyesdate[k1] = time.strftime("%d %b %Y", time.localtime(new1[l]['date']))
				print('ifyes',ifyes)
				l = l - 1
				k1 = k1 + 1

		for u in NO:
			print('\t \t postno', u)
			if u in ifyes:
				del ifyes[u]
			if u in ifyestext:
				del ifyestext[u]
			if u in ifyesdate:
				del ifyesdate[u]
		ifyes = list(ifyes.values())
		ifyestext = list(ifyestext.values())
		ifyesdate = list(ifyesdate.values())
		return [ifyes, ifyestext, ifyesdate]
	else:
		return False
