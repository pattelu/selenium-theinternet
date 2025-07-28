from pages.drag_and_drop_page import DragAndDropPage

def test_drag_and_drop(chrome_browser):
    dad_page = DragAndDropPage(chrome_browser)
    dad_page.open_page()
    result = dad_page.drag_and_drop("a", "b")

    assert result, "Drag doesn't work. Columns are in incorrect order."