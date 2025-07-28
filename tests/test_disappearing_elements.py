from pages.disappearing_elements_page import DisappearingElementsPage

def test_disappearing_elements(chrome_browser):
    de_page = DisappearingElementsPage(chrome_browser)
    de_page.open_page()
    result = de_page.check_buttons()

    assert result, "Not all buttons are displayed."