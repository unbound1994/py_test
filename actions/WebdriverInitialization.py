from selenium import webdriver


class BrowserInit:

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--start-maximized')
        # self.chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)

    def initialization_browser(self):
        yield self.driver
        print("\nquit browser..")
        self.driver.quit()
        self.driver.close()

