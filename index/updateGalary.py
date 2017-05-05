import vk
import time
import requests
from index import models

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
            if int(m_id)>int(start_id):
                print(small, '\n',big)
                try:
                    models.Gallary.objects.get(photo_id=this_object_id)
                except RealEstateListing.DoesNotExist:
                    file_small = requests.get(url='https://api.telegram.org/bot{0}/getFile?file_id={1}'.format(token, small)).json()
                    url_small = 'https://api.telegram.org/file/bot{0}/{1}'.format(token, file_small['result']['file_path'])
                    file_big = requests.get(url='https://api.telegram.org/bot{0}/getFile?file_id={1}'.format(token, big)).json()
                    url_big = 'https://api.telegram.org/file/bot{0}/{1}'.format(token, file_big['result']['file_path'])
                    models.Gallary.objects.create(photo_big=requests.get(url_big).content, photo_small=requests.get(url_small).content, photo_id=int(m_id))
        except:
            pass
