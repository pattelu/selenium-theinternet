from pages.checkboxes_page import CheckboxesPage

def test_checbox_selected(chrome_browser):
    chb_page = CheckboxesPage(chrome_browser)
    chb_page.open_page()

    # Checkbox click on
    checkbox_1 = chb_page.select_checkbox("1")

    assert checkbox_1.is_selected(), "Checbox 1 was not selected."

def test_checbox_deselected(chrome_browser):
    chb_page = CheckboxesPage(chrome_browser)
    chb_page.open_page()

    # Checkbox click off
    checkbox_2 = chb_page.select_checkbox("2")

    assert not checkbox_2.is_selected(), "Checkbox 2 was not deselected."