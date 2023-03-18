from selenium.webdriver.common.by import By
from actions.actions import BrowserInit


class LoginPage(BrowserInit):

    TITLE = (By.CLASS_NAME, 'pos-logo')
    LOGIN_FORM = (By.CSS_SELECTOR, 'login_form >h1')
    LOGIN = (By.ID, 'login')
    PASSWORD = (By.ID, 'password')
    PASSWORD_EYE = (By.CLASS_NAME, '.password-control')
    FORGOT_PASSWORD = (By.XPATH, '//*[text() = \'Забыли пароль?\']')
    ENTER_BUTTON = (By.ID, 'login-btn')

    # Reset passwd locators block
    RESET_PASSWD_FORM = (By.ID, 'reset_password_form')
    FORM_TITLE = (By.ID, '#reset_password_form > h1')
    REST_LOGIN = (By.ID, 'login_reset')
    RETURN_AUTHORIZE_FORM = (By.XPATH, '//*[text() = \'Вернуться к авторизации\']')
    SEND_PASSWD_TO_EMAIL = (By.ID, 'reset_btn')
    SEND_PASSWD_TO_SMS = (By.ID, 'reset_btn_sms')
    USER_NOY_FOUND = (By.XPATH, '//*[text() = \'Пользователь не найден.\']')
    ERROR_MSG = (By.XPATH, '//*[text() = \'При отправке возникла ошибка\']')
    SUCCESS_MSG = (By.XPATH, '//*[text() = \'Ссылка на восстановление пароля успешно отправлена\']')

    COMPANY_SELECT = (By.ID, 'select2-access_company-container')
    COMPANY_SEARCH = (By.CLASS_NAME, 'select2-search__field')
    COMPANY_RESULTS = (By.ID, 'select2-access_company-results')

