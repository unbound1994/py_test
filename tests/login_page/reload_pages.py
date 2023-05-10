import requests

from read_env import read_env

from actions.actions import *
from actions.notify_telegram import sendMessage
from selenium.webdriver.common.by import By

read_env("../.env")

driver.close()

data = ''
url = 'https://edu.21-school.ru/services/paper/load_actual_papers?organizationId=6bfe3c56-0211-4fe1-9e59' \
      '-51616caac4dd'

LOGIN = (By.CLASS_NAME, "MuiInputBase-input.MuiFilledInput-input.css-2bxn45")
PASSWD = (By.CLASS_NAME, "MuiInputBase-input.MuiFilledInput-input.MuiInputBase-inputAdornedEnd.css-ftr4jk")
BUTTON = (By.CSS_SELECTOR, "#login > div > div > div.jss4 > div > div > form > div.jss22 > button")


def getDataFromJSON():
    global data

    data = requests.get(url).json()['data']
    return data


while not getDataFromJSON():
    print("Checking... Actual data is - " + str(data))
    time.sleep(5)


if data:
    print("Available data. Restart browser session!\n")

    driver.start_session({})
    driver.get("https://edu.21-school.ru/projects/code-review")

    find_elem(LOGIN).send_keys(os.environ.get('LOG'))
    find_elem(PASSWD).send_keys(os.environ.get('PASSW'))

    waiter(1)

    print("Ready for login!")
    find_elem(BUTTON).click()

sendMessage('Кажется пришел проект на ревью!', 239402268)
