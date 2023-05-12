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

    find_elem(LOGIN).send_keys("os.environ.get('LOG')")
    find_elem(PASSWD).send_keys("os.environ.get('PASSW')")

    waiter(1)

    print("Ready for login!")
    find_elem(BUTTON).click()

    CHECK = (By.XPATH, '//*[text() = \'You have no projects for review\']')
    DOUBLE_CHECK = (By.XPATH, '//a[@href="'+url+'"]')
    check_text = 'You have no projects for review'

    flag_checker = True


    # нейронка, не иначе
    try:
        while flag_checker:
            if not find_elem(CHECK):
                screenShooter()
                sendMessage('Блока "no projects" нет. Возможно пришел проект на ревью!', 1670987669)
                flag_checker = False
            elif find_elem(CHECK):
                if find_elem(CHECK).text == check_text:
                    driver.refresh()
                    flag_checker = True
                    waiter(4)
            elif not find_elem(CHECK) & find_elem(DOUBLE_CHECK):
                screenShooter()
                sendMessage('Блоки поменялись. Кажется пришел проект на ревью!', 1670987669)
                flag_checker = False
            elif not find_elem(CHECK):
                if not find_elem(DOUBLE_CHECK):
                    screenShooter()
                    sendMessage('Кажется зависла страница. Нет блока "no projects" и вкладки Review!', 1670987669)
                    flag_checker = False
            else:
                screenShooter()
                sendMessage('Ни одно из условий не сработало!', 1670987669)
                break
    except Exception as e:
        screenShooter()
        print("Вообще херня произошла, которая никак не учитывается. Сделан скриншот - ", e)
