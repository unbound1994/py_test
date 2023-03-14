from selenium.webdriver.common.by import By
from actions.actions import BrowserInit


class LoginPage(BrowserInit):

    TITLE = (By.CLASS_NAME, 'pos-logo')
    LOGIN_FORM = (By.CSS_SELECTOR, 'login_form >h1')
    LOGIN = (By.ID, 'login')
    PASSWORD = (By.ID, 'password')
    FORGOT_PASSWORD = (By.XPATH, '//*[text() = \'Забыли пароль?\']')
    ENTER_BUTTON = (By.ID, 'login-btn')
