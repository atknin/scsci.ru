import vk
import time
from index import models
import requests
import os
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

def updateGalary():
    token = '311079347:AAFtMNwa4ziqcewP_5cK2d1m3JWulpsmtZg'
    method = 'getUpdates'
    getpost = requests.get(url='https://api.telegram.org/bot{0}/{1}'.format(token, method),).json()
    try:
        updates = getpost['result']
    except Exception as e:
        print(str(e))

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

                img_temp_big = NamedTemporaryFile(delete=True)
                img_temp_big.write(requests.get(url_big).content)
                img_temp_big.flush()

                img_temp_small = NamedTemporaryFile(delete=True)
                img_temp_small.write(requests.get(url_small).content)
                img_temp_small.flush()

                a = models.Gallary(photo_id=int(m_id))
                a.photo_big.save(os.path.basename(url_big), File(img_temp_big))
                a.photo_small.save(os.path.basename(url_small), File(img_temp_small))
                a.save()




        except Exception as e:
            print(str(e))
