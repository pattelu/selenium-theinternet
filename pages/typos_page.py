from selenium.webdriver.common.by import By

class TyposPage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get("https://the-internet.herokuapp.com/typos")

    @property
    def get_text(self):
        return self.driver.find_element(By.XPATH, '//*[@id="content"]/div/p[2]').text