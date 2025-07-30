from pages.entry_ad_page import EntryAdPage

def test_entry_ad(chrome_browser):
    ead_page = EntryAdPage(chrome_browser)
    ead_page.open_page()
    result = ead_page.modal_window_visible()

    assert result, "Entry Ad is not displayed."