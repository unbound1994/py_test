from actions.actions import *
from selenium.webdriver.common.by import By


def test_page():
    url = 'https://edu.21-school.ru/projects/code-review'
    open_page(url)

    CHECK = (By.CLASS_NAME, 'jss1169.jss1173.jss1874')
    check_text = 'You have no projects for review'

    waiter(5)

    while find_elem(CHECK).text == check_text:
        waiter(2)
        driver.refresh()

