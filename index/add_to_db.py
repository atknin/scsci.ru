# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
import time
# https://api.telegram.org/bot285455287:AAERVWhSH53FLL1zWERx_u7f7pJJMMP97qA/getFile?file_id=AgADAgADwqcxG73a4UsRleHt4CKl4Uc6tw0ABEd6NT3JTUDSGG8CAAEC
# https://api.telegram.org/file/bot285455287:AAERVWhSH53FLL1zWERx_u7f7pJJMMP97qA/photos/file_8.jpg

token = '285455287:AAERVWhSH53FLL1zWERx_u7f7pJJMMP97qA'
method = 'getUpdates'
print('started...')
getpost = requests.get(
                url='https://api.telegram.org/bot{0}/{1}'.format(token, method),).json()

start_id = int(getpost['result'][-1]['message']['message_id'])
while True:
    getpost = requests.get(
                    url='https://api.telegram.org/bot{0}/{1}'.format(token, method),).json()
    a = getpost['result'][-1]['message']['message_id']
    print(start_id,a)
    if start_id < int(a):
        mes = getpost['result'][-1]['message']['text']
        r = requests.post('http://scsci.ru/add_to_db/', data = {'message':mes})
        print('posted',r)
    else:
        print('no new message')
    time.sleep(10)
# print(a)
#
# print(r)



















# file_id = getpost['result'][-1]['message']['photo'][1]['file_id']
# print(file_id)
#
# file_path = requests.get(url='https://api.telegram.org/bot{0}/getFile?file_id={1}'.format(token, file_id)).json()
# urlll = 'https://api.telegram.org/file/bot{0}/{1}'.format(token, file_path['result']['file_path'])
# print(urlll)
#
#
# # file_1 = requests.get(url='https://api.telegram.org/file/bot{0}/{1}'.format(token, method_file))
# # print(file_1)
# f = open('00000001.jpg','wb')
# f.write(requests.get(urlll).content)
# f.close()
