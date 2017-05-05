import vk
import time
from index import models
from urllib.parse import urlparse
import os
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
            print(small, '\n',big)
            if models.Gallary.objects.filter(photo_id=int(m_id)).exists():
                pass
            else:
                file_small = requests.get(url='https://api.telegram.org/bot{0}/getFile?file_id={1}'.format(token, small)).json()
                url_small = 'https://api.telegram.org/file/bot{0}/{1}'.format(token, file_small['result']['file_path'])
                file_big = requests.get(url='https://api.telegram.org/bot{0}/getFile?file_id={1}'.format(token, big)).json()
                url_big = 'https://api.telegram.org/file/bot{0}/{1}'.format(token, file_big['result']['file_path'])
                models.Gallary.objects.create(photo_big=os.path.basename(urlparse(url_big).path), photo_small=os.path.basename(urlparse(url_small).path), photo_id=int(m_id))
                print('aded')
        except:
            pass
