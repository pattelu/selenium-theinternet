from selenium.webdriver.common.by import By

class DisappearingElementsPage():
    def __init__(self, driver):
        self.driver = driver
    
    def open_page(self):
        self.driver.get("https://the-internet.herokuapp.com/disappearing_elements")

    def check_buttons(self):
        items = self.driver.find_elements(By.TAG_NAME, "li")
        count = 0
        buttons_number = 5

        for item in items:
            count += 1
        if count == buttons_number:
            return True
        else:
            return False