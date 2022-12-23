from selenium import webdriver

GET_YANDEX_DISK_API_URL = "https://yandex.ru/dev/disk/poligon/"
GET_PHOTO_URL = "https://www.pexels.com/ru-ru/search/"

class BaseYandexDisk(webdriver.Chrome):


    def __del__(self):
        self.close()
        self.quit()
        print("Браузер закрыт")

    def exit(self):
        self.__del__()