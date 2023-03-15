from actions.actions import *
from login_locators.LoginLocators import LoginPage
from actions.DBConnection import *

path = "../../.env"
read_env(path)


def test_login():
    open_page(os.environ.get('URL_TEST'))
    waiter(2)
    find_elem(LoginPage.LOGIN)
    writer(LoginPage.LOGIN, os.environ.get('LOGIN'))

    waiter(5)
