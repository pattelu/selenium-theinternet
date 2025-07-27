from selenium.webdriver.common.by import By

class CheckboxesPage():
    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get("https://the-internet.herokuapp.com/checkboxes")

    def select_checkbox(self, name):
        checkbox = self.driver.find_element(By.XPATH, f'//*[@id="checkboxes"]/input[{name}]')
        checkbox.click()
        return checkbox
