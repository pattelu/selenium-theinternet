from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get("https://the-internet.herokuapp.com/")

    def abtest_btn(self):
        self.driver.find_element(By.LINK_TEXT, "A/B Testing").click()