from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from time import sleep
from config import GET_YANDEX_DISK_API_URL, BaseYandexDisk

import requests

class YandexDisk(BaseYandexDisk):
    def get_token_start(self):
        self.get(GET_YANDEX_DISK_API_URL)
        sleep(3)
        self.switch_to.frame(self.find_element(
            By.XPATH,
            "/html/body/div[3]/div/div/span/section/div[1]/div[1]/div/section/"
            "div/div/section/div/div/div/div[1]/div/section/div/div/div/div[4]/section/div/div/iframe"))
        self.find_element(By.XPATH, "/html/body/div/section/div[1]/div/a").click()
        sleep(3)
        self.switch_to.default_content()


    def login_input(self, login: str) -> bool:
        self.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/"
            "div/div/div/div[1]/form/div[2]/div/div[2]/span/input").send_keys(login)

        self.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/"
            "div/div/div/div[1]/form/div[4]/button").click()
        sleep(3)
        try:
            self.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/"
                                        "div/div[2]/div[3]/div/div/div/div[1]/form/div[2]/div/div[2]/div")
            print("Такого аккаунта не существует")
            return False
        except NoSuchElementException:
            sleep(3)
            return True


    def password_input(self, password: str) -> bool:
        self.find_element(
            By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/"
                      "div/div/div/form/div[2]/div[1]/span/input"
        ).send_keys(password)
        self.find_element(
            By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]"
                      "/div/div/div/form/div[3]/button"
        ).click()
        try:
            self.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]"
                                            "/div/div/div/form/div[2]/div[1]/div")
            print("Неверный пароль")
            return False
        except NoSuchElementException:
            sleep(3)
            return True


    def get_token(self) -> None:
        self.switch_to.frame(self.find_element(By.XPATH, "/html/body/div[3]/div/div/span/section/div[1]/div[1]"
            "/div/section/div/div/section/div/div/div/div[1]/div/section/div/div/div/div[4]/section/div/div/iframe"))
        self.disk_token = self.find_element(By.XPATH, "/html/body/div/section/div[1]/span/input").get_attribute('value')


    @staticmethod
    def upload_files(token: str, urls: list) -> None:
        requests.put("https://cloud-api.yandex.net/v1/disk/resources",
                     headers={"Authorization": f"OAuth {token}"},
                     params={"path": "/IMG/"})
        for num, url in enumerate(urls):
            print(requests.post(
                "https://cloud-api.yandex.net/v1/disk/resources/upload",
                headers={"Authorization": f"OAuth {token}"},
                params={
                    "url": url,
                    "path": f"/IMG/photo_{num + 1}.jpg",
                }).status_code)
