import pytest
from pages.basic_auth_page import BasicAuthPage
from selenium.common.exceptions import NoSuchElementException


@pytest.mark.trio
async def test_success_sign_in(chrome_browser):
    sign_page = BasicAuthPage(chrome_browser)
    await sign_page.send_credentials()
    success = sign_page.get_success
    assert success == "Congratulations! You must have the proper credentials.", "User wasn't navigated to logged page."

@pytest.mark.trio
async def test_failed_sign_in(chrome_browser):
    signin_page = BasicAuthPage(chrome_browser)
    await signin_page.send_credentials("admin", "password")
    try:
        fail = signin_page.get_success
        assert False, "User should not be navigated to logged page."
    except NoSuchElementException:
        assert True, "User was naviagated to logged page."