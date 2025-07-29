from pages.status_codes_page import StatusCodePage

def test_status_codes_200(chrome_browser):
    sc_page = StatusCodePage(chrome_browser)
    sc_page.open_page()
    
    result = sc_page.verify_status("200")

    assert result, "Status Code: 200 - Fail\n"

def test_status_codes_301(chrome_browser):
    sc_page = StatusCodePage(chrome_browser)
    sc_page.open_page()

    result = sc_page.verify_status("301")

    assert result, "Status Code: 301 - Fail\n"

def test_status_codes_404(chrome_browser):
    sc_page = StatusCodePage(chrome_browser)
    sc_page.open_page()

    result = sc_page.verify_status("404")

    assert result, "Status Code: 404 - Fail\n"
    
def test_status_codes_500(chrome_browser):
    sc_page = StatusCodePage(chrome_browser)
    sc_page.open_page()

    result = sc_page.verify_status("500")

    assert result, "Status Code: 500 - Fail\n"
    