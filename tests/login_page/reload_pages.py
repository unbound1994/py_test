from actions.actions import *
from selenium.webdriver.common.by import By

from actions.notify_telegram import sendMessage


def test_page():
    url = 'https://edu.21-school.ru/projects/code-review'
    open_page(url)

    waiter(30)

    CHECK = (By.XPATH, '//*[text() = \'You have no projects for review\']')
    check_text = 'You have no projects for review'

    try:
        while find_elem(CHECK).text == check_text:
            driver.refresh()
            waiter(4)
    except NoSuchElementException:
        sendMessage('Кажется пришел проект на ревью!', 1670987669)

