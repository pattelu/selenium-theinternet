from pages.typos_page import TyposPage

def test_typos(chrome_browser):
    tp_page = TyposPage(chrome_browser)
    tp_page.open_page()
    text = tp_page.get_text

    assert text == "Sometimes you'll see a typo, other times you won't.", "Wrong text was displayed."