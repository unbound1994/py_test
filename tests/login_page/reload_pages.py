from actions.actions import *
from selenium.webdriver.common.by import By

from actions.notify_telegram import sendMessage


def screenShooter():
    name = time.strftime("%d.%m.%Y_%H-%M-%S")
    fullName = "Screenshot_" + name + ".png"
    path = unipath.Path(__file__).parent.parent.parent + "\\" + "Screenshots\\"

    if not os.path.exists(path):
        os.makedirs(path)

    fullPath = path + fullName
    screenshot = open(r"" + fullPath, "wb")
    screenshot.write(driver.get_screenshot_as_png())


def test_page():
    LOGIN = (By.CLASS_NAME, "MuiInputBase-input.MuiFilledInput-input.css-2bxn45")
    PASSWD = (By.CLASS_NAME, "MuiInputBase-input.MuiFilledInput-input.MuiInputBase-inputAdornedEnd.css-ftr4jk")
    BUTTON = (By.CSS_SELECTOR, "#login > div > div > div.jss4 > div > div > form > div.jss22 > button")

    url = 'https://edu.21-school.ru/projects/code-review'
    open_page(url)

    find_elem(LOGIN).send_keys(os.environ.get('LOG'))
    find_elem(PASSWD).send_keys(os.environ.get('PASSW'))

    waiter(1)

    print("Ready for login!")
    find_elem(BUTTON).click()

    CHECK = (By.XPATH, '//*[text() = \'You have no projects for review\']')
    SECOND_CHECK = (By.XPATH, '//*[text() = \'Available for code review\']')

    flag_checker = True
    waitTime = 0
    chatID = 1670987669

    # нейронка, не иначе
    try:
        while flag_checker:
            if not find_elem(SECOND_CHECK):
                driver.refresh()
                waitTime = 4
                waiter(waitTime)
                flag_checker = True
            elif not find_elem(CHECK):
                if find_elem(SECOND_CHECK):
                    screenShooter()
                    sendMessage('Кажется пришел проект на ревью!', chatID)
                    flag_checker = False
            elif not find_elem(CHECK):
                if not find_elem(SECOND_CHECK):
                    screenShooter()
                    driver.refresh()
                    waitTime = 4
                    waiter(waitTime)
                    sendMessage('Кажется зависла страница. Нет блока "no projects" и вкладки "Available for"!', chatID)
                    flag_checker = True
            else:
                screenShooter()
                sendMessage('Ни одно из условий не сработало!', chatID)
                break
    except Exception as e:
        screenShooter()
        print("Вообще херня произошла, которая никак не учитывается. Сделан скриншот - ", e)


test_page()
