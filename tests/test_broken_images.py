from pages.broken_images_page import BrokenImagesPage

def test_broken_images(chrome_browser):
    result = True
    text = ""
    bi_page = BrokenImagesPage(chrome_browser)
    bi_page.open_page()
    images = bi_page.find_images()
    for image in images:
        image_result = bi_page.verify_image(image)
        if not image_result:
            text += f"{image} is broken.\n"
            result = False

    assert result, text