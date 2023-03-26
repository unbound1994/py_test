from selenium.webdriver.common.by import By
from actions.actions import BrowserInit


class LoginPage(BrowserInit):

    # First login page
    TITLE = (By.CLASS_NAME, 'pos-logo')
    LOGIN_FORM = (By.CSS_SELECTOR, 'login_form >h1')
    LOGIN = (By.ID, 'login')
    PASSWORD = (By.ID, 'password')
    PASSWORD_EYE = (By.CLASS_NAME, '.password-control')
    FORGOT_PASSWORD = (By.XPATH, '//*[text() = \'Забыли пароль?\']')
    ENTER_BUTTON_FIRST = (By.ID, 'login-btn')

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

    # Second login page
    COMPANY_SELECT = (By.ID, 'select2-access_company-container')
    COMPANY_SEARCH_INPUT = (By.CSS_SELECTOR, 'body > span > span > span.select2-search.select2-search--dropdown > input')
    COMPANY_SEARCH_ERROR = (By.XPATH, '//*[text() = \'Невозможно загрузить результаты\']')
    COMPANY_RESULTS = (By.CLASS_NAME, 'select2-results__options')
    COMPANY_RESULTS_VARIANT = (By.TAG_NAME, 'li')
    TRADES_SELECT = (By.XPATH, '//span[@class=\'select2-selection__rendered\' and @id=\'select2-access_trade-container\']')
    TRADES_SEARCH = (By.XPATH, '//input[@class=\'select2-search__field\' and @aria-controls=\'select2-access_trade-results\']')
    TRADES_SEARCH_ERROR = (By.XPATH, '//*[text() = \'Невозможно загрузить результаты\']')
    TRADES_RESULTS = (By.CLASS_NAME, 'select2-results__options')
    TRADES_RESULTS_VARIANT = (By.TAG_NAME, 'li')
    ENTER_BUTTON_SECOND = (By.ID, 'second-login-btn')
    BACK_TO_LOGIN = (By.CLASS_NAME, 'back-to-login')

    FORM = (By.CLASS_NAME, 'form')
