from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support.ui import WebDriverWait

class ContextMenuPage():
    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get("https://the-internet.herokuapp.com/context_menu")

    def right_click_box(self):
        context = self.driver.find_element(By.ID, "hot-spot")
        ActionChains(self.driver) \
            .context_click(context) \
                .perform()
    
    def is_prompt_visible(self):
        wait = WebDriverWait(self.driver, 2)
        alert = wait.until(lambda d : d.switch_to.alert)
        text = alert.text
        return text