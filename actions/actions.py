import unittest
import time
import os

import unipath
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from actions.WebdriverInitialization import BrowserInit
from login_locators.LoginLocators import LoginPage

"""Базовые методы для всех файлов"""

driver = BrowserInit().driver


def open_page(url):
    driver.get(url)


def is_element_present(locator):
    try:
        driver.find_element(*locator)
    except NoSuchElementException:
        return False
    return True


def find_elem(locator):
    try:
        return driver.find_element(*locator)
    except NoSuchElementException:
        return False


def writer(locator, message, *args):
    driver.find_element(*locator).send_keys(message)


def waiter(sec):
    time.sleep(sec)


def wait_until(sec, locator, options):
    options_list = {
        1: EC.element_to_be_clickable(locator),
        2: EC.presence_of_element_located(locator),
        3: EC.visibility_of_element_located(locator)
    }
    WebDriverWait(driver, sec).until(options_list.get(options))


"""Предварительный логин перед действиями в платформе"""


def fast_login(login, passwd, company_name=None, trade_name=None):
    open_page(os.environ.get('URL_TEST'))

    find_elem(LoginPage.LOGIN).click()
    writer(LoginPage.LOGIN, login)

    find_elem(LoginPage.PASSWORD).click()
    writer(LoginPage.PASSWORD, passwd)

    find_elem(LoginPage.ENTER_BUTTON_FIRST).click()

    find_elem(LoginPage.COMPANY_SELECT).click()
    find_elem(LoginPage.COMPANY_SEARCH_INPUT).click()
    writer(LoginPage.COMPANY_SEARCH_INPUT, company_name)

    if is_element_present(LoginPage.COMPANY_SEARCH_ERROR):
        find_elem(LoginPage.COMPANY_SEARCH_INPUT).send_keys(Keys.SPACE)
        waiter(1)
        find_elem(LoginPage.COMPANY_SEARCH_INPUT).send_keys(Keys.ENTER)
    else:
        find_elem(LoginPage.COMPANY_SEARCH_INPUT).send_keys(Keys.SPACE)
        waiter(1)
        find_elem(LoginPage.COMPANY_SEARCH_INPUT).send_keys(Keys.ENTER)

    waiter(2)
    find_elem(LoginPage.TRADES_SELECT).click()
    find_elem(LoginPage.TRADES_SEARCH).click()
    writer(LoginPage.TRADES_SEARCH, trade_name)

    if is_element_present(LoginPage.TRADES_SEARCH_ERROR):
        find_elem(LoginPage.TRADES_SEARCH).send_keys(Keys.SPACE)
        waiter(1)
        find_elem(LoginPage.TRADES_SEARCH).send_keys(Keys.RETURN)
    else:
        waiter(1)
        find_elem(LoginPage.TRADES_SEARCH).send_keys(Keys.RETURN)

    find_elem(LoginPage.ENTER_BUTTON_SECOND).click()


if __name__ == '__main__':
    unittest.main()
