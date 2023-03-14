from selenium import webdriver


class BrowserInit:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.chr_options = webdriver.ChromeOptions()

    def inition_browser(self):
        yield self.driver
        print("\nquit browser..")
        self.driver.quit()
        self.driver.close()

    def options(self):
        return self.chr_options
