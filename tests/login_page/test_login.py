import os
from read_env import read_env

from actions.actions import *
from login_locators.login_page import LoginPage


path = "../../.env"
read_env(path)


def test_login():
    open_page(os.environ.get('URL_TEST'))
    waiter(2)
    find_elem(LoginPage.LOGIN)
    writer(LoginPage.LOGIN, os.environ.get('LOGIN'))

    waiter(5)
