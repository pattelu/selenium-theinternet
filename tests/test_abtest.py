from pages.home_page import HomePage
from pages.abtest_page import ABtestPage
from selenium.webdriver.common.by import By

def test_abtest(chrome_browser):
    homepage = HomePage(chrome_browser)
    homepage.open_page()
    homepage.abtest_btn()

    abtest_page = ABtestPage(chrome_browser)
    header_title = abtest_page.header_title

    assert header_title in ["A/B Test Control", "A/B Test Variation 1"], "User was not navigated to one of two variant of the page."
