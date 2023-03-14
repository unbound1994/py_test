import unittest
import time

from selenium.common.exceptions import NoSuchElementException
from actions.webdriver_inition import BrowserInit

"""Базовые методы для всех файлов"""

driver = BrowserInit().driver


def open_page(url):
    driver.get(url)


def is_element_present(method, locator):
    try:
        driver.find_element(method, locator)
    except NoSuchElementException:
        return False
    return True


def find_elem(locator):
    print(*locator)
    driver.find_element(*locator)


def writer(locator, message):
    driver.find_element(*locator).send_keys(message)


def waiter(sec):
    time.sleep(sec)


if __name__ == '__main__':
    unittest.main()
