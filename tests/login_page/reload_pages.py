from actions.actions import *
from selenium.webdriver.common.by import By

from actions.notify_telegram import sendMessage


def test_page():
    url = 'https://edu.21-school.ru/projects/code-review'
    open_page(url)

    waiter(30)

    CHECK = (By.CLASS_NAME, 'jss1169.jss1173.jss1874')
    check_text = 'You have no projects for review'

    waiter(5)

    while find_elem(CHECK).text == check_text:
        waiter(2)
        driver.refresh()

    sendMessage('Кажется пришел проект на ревью!', 1670987669)
