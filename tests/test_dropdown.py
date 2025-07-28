from pages.dropdown_page import DropDownPage

def test_dropdown(chrome_browser):
    dd_page = DropDownPage(chrome_browser)
    dd_page.open_page()
    selection = dd_page.select_item("1")

    assert selection.is_selected, "Correct item is not selected."