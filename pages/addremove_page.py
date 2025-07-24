from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddRemovePage():
    def __init__(self, driver):
        self.driver = driver
    
    def open_page(self):
        self.driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

    def add_element_btn(self):
        self.driver.find_element(By.XPATH, '//*[@id="content"]/div/button').click()

    def get_delete_btn(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "added-manually"))
        )
        
    def delete_btn(self):
        self.driver.find_element(By.CLASS_NAME, "added-manually").click()

    def is_delete_btn(self):
        elements = self.driver.find_elements(By.CLASS_NAME, "added-manually")
        return elements and elements[0].is_displayed()