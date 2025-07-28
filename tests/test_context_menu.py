from pages.context_menu_page import ContextMenuPage
import time
def test_context_menu(chrome_browser):
    cm_page = ContextMenuPage(chrome_browser)
    cm_page.open_page()
    cm_page.right_click_box()
    text = cm_page.is_prompt_visible()
    
    assert "You selected a context menu" == text, "Prompt is not visible or text inside is diffrent."
