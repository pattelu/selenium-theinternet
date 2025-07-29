from selenium.webdriver.common.by import By
import requests

class StatusCodePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get("https://the-internet.herokuapp.com/status_codes")

    def verify_status(self, number):
        self.driver.find_element(By.LINK_TEXT, f"{number}").click()

        url = requests.get(self.driver.current_url)

        if url.status_code == int(number):
            return True
        else:
            return False
