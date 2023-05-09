import time
import requests

from actions.notify_telegram import sendMessage


def reload_page():
    url = 'https://edu.21-school.ru/services/paper/load_actual_papers?organizationId=6bfe3c56-0211-4fe1-9e59' \
          '-51616caac4dd'

    request = requests.get(url)
    return request.json()['data']


while not reload_page():
    print("Checking... Actual data is - " + str(reload_page()))
    time.sleep(5)

sendMessage('Кажется пришел проект на ревью!', 1670987669)
