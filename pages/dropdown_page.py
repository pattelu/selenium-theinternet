from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class DropDownPage():
    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get("https://the-internet.herokuapp.com/dropdown")
    
    def select_item(self, item):
        dropdown = self.driver.find_element(By.ID, "dropdown")
        select = Select(dropdown)

        element = self.driver.find_element(By.CSS_SELECTOR, f'option[value="{item}"]')

        select.select_by_value(item)

        return element