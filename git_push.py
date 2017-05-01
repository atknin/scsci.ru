# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import paramiko
import os
from time import gmtime, strftime
commit = strftime("%Y-%m-%d %H:%M:%S", gmtime())

print(os.system('git checkout alex'))
print(os.system('git add .'))

print(os.system('git rm --cached git_do.py'))
print(os.system('git commit -m "'+ 'alex_' + commit + '"'))
print(os.system('git push origin alex'))
# host = 'x-rays.world'
host = '62.109.6.12'
user = 'user'
secret = 'aD3AO6S60moR'
port = 22
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=secret, port=port)

channel = client.invoke_shell()
stdin = channel.makefile('wb')
stdout = channel.makefile('rb')
stdin.write('''
	cd env/sostrov
	git merge alex
	touch sostrov_uwsgi.ini
	''')
# git fetch --all
#
# 	git reset --hard origin/master
# https://github.com/atknin/x-rays.git
for line in stdout:
	print(line)

client.close()
stdout.close()
stdin.close()



# print('done, but not closed.')
# client.close()
# stdout.close()
# stdin.close()
print('done and closed.')
