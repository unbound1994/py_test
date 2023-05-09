import unipath

from actions.actions import *
from selenium.webdriver.common.by import By

from actions.notify_telegram import sendMessage


def test_page():
    name = time.strftime("%d.%m.%Y_%H-%M-%S")
    fullName = "Screenshot_" + name + ".png"
    path = unipath.Path(__file__).parent.parent.parent + "\\" + "Screenshots\\"

    if not os.path.exists(path):
        os.makedirs(path)

    fullPath = path + fullName
    screenshot = open(r""+fullPath, "wb")

    url = 'https://edu.21-school.ru/projects/code-review'
    open_page(url)

    waiter(30)

    CHECK = (By.XPATH, '//*[text() = \'You have no projects for review\']')
    check_text = 'You have no projects for review'

    try:
        while find_elem(CHECK).text == check_text:
            driver.refresh()
            waiter(4)
    except Exception as e:
        print("Something wrong - ", e)

    if find_elem(CHECK).text != check_text:
        screenshot.write(driver.get_screenshot_as_png())

    sendMessage('Кажется пришел проект на ревью!', 1670987669)
