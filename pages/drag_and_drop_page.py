from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class DragAndDropPage():
    def __init__(self, driver):
        self.driver = driver
    
    def open_page(self):
        self.driver.get("https://the-internet.herokuapp.com/drag_and_drop")

    def drag_and_drop(self, column_one, column_two):
        draggable = self.driver.find_element(By.ID, f'column-a')
        droppable = self.driver.find_element(By.ID, f'column-b')
        ActionChains(self.driver) \
            .drag_and_drop(draggable, droppable) \
                .perform()

        header_one = self.driver.find_element(By.XPATH, f'//*[@id="column-a"]/header').text
        header_two = self.driver.find_element(By.XPATH, f'//*[@id="column-b"]/header').text

        if header_one == "B" and header_two == "A":
            return True
        else:
            return False