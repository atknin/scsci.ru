import vk
import time
from index import models
import urllib
import requests
import os
from django.core.files import File

def updateGalary():
    token = '311079347:AAFtMNwa4ziqcewP_5cK2d1m3JWulpsmtZg'
    method = 'getUpdates'
    getpost = requests.get(url='https://api.telegram.org/bot{0}/{1}'.format(token, method),).json()
    try:
        updates = getpost['result']
    except Exception as e:
        pass

    for a in updates:
        m_id = a['message']['message_id']
        try:
            small = a['message']['photo'][1]['file_id']
            big = a['message']['photo'][-1]['file_id']
            if models.Gallary.objects.filter(photo_id=int(m_id)).exists():
                pass
            else:
                file_small = requests.get(url='https://api.telegram.org/bot{0}/getFile?file_id={1}'.format(token, small)).json()
                url_small = 'https://api.telegram.org/file/bot{0}/{1}'.format(token, file_small['result']['file_path'])
                file_big = requests.get(url='https://api.telegram.org/bot{0}/getFile?file_id={1}'.format(token, big)).json()
                url_big = 'https://api.telegram.org/file/bot{0}/{1}'.format(token, file_big['result']['file_path'])
                result_small = urllib.urlretrieve(url_small)
                result_big = urllib.urlretrieve(url_big)
                a = models.Gallary(photo_id=int(m_id))
                a.photo_big.save(os.path.basename(url_big), File(open(result_big[0]))) 
                a.photo_small.save(os.path.basename(url_small), File(open(result_small[0])))
                a.save()
        except:
            pass
