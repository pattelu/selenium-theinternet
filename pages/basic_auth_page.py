import base64 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v137.network import Headers

class BasicAuthPage:
    def __init__(self, driver):
        self.driver = driver

    async def send_credentials(self, username="admin", password="admin"):
        async with self.driver.bidi_connection() as connection:
            await connection.session.execute(connection.devtools.network.enable())

            credentials = base64.b64encode(f"{username}:{password}".encode()).decode()
            auth = {'authorization': 'Basic ' + credentials}
            await connection.session.execute(connection.devtools.network.set_extra_http_headers(Headers(auth)))
            

            self.driver.get("https://the-internet.herokuapp.com/basic_auth")


    @property
    def get_success(self):
        return self.driver.find_element(By.TAG_NAME, "p").text



    