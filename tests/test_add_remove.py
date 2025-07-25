import pytest
from pages.add_remove_page import AddRemovePage
from selenium.webdriver.common.by import By
import time


def test_add_element(chrome_browser):
    ar_page = AddRemovePage(chrome_browser)
    ar_page.open_page()
    ar_page.add_element_btn() 

    assert ar_page.get_delete_btn().is_displayed(), "Delete button is not visible, but should be visible."


def test_remove_element(chrome_browser):
    ar_page = AddRemovePage(chrome_browser)
    ar_page.open_page()
    ar_page.add_element_btn()
    ar_page.delete_btn()

    assert not ar_page.is_delete_btn(), "Delete button is visible, but should not be visible."



