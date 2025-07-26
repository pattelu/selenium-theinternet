import requests
from selenium.webdriver.common.by import By

class BrokenImagesPage():
    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get("https://the-internet.herokuapp.com/broken_images")

    def find_images(self):
        images = self.driver.find_elements(By.CSS_SELECTOR, "div.example img")
        image_url = []
        for image in images:
            image_url.append(image.get_attribute("src"))

        return image_url

    def verify_image(self, image):
        respond = requests.get(image)
        if respond.status_code == 200:
            return True
        else:
            return False