from selenium.webdriver.common.by import By

class ABtestPage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def header_title(self):
        return self.driver.find_element(By.TAG_NAME, "h3").text