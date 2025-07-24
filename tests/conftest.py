import pytest
from selenium import webdriver

service = webdriver.ChromeService()
driver = webdriver.Chrome(service=service)

@pytest.fixture()
def chrome_browser():
    driver = webdriver.Chrome()

    driver.implicitly_wait(10)

    yield driver

    driver.quit()