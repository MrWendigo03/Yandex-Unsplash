from yandex_disk import YandexDisk
from get_photo import get_url_photo


if __name__ == "__main__":
    disk1 = get_url_photo("something")
    # disk1.get_pho(input("Введите объект поиска: "))
    disk = yandex_disk.YandexDisk("drivers/chromedriver.exe")
    disk.get_token_start()
    disk.login_input("N0ch1Gu4rd14n")
    disk.password_input("Z1rk0n1s")
    disk.get_token()
    print(disk.disk_token)
    yandex_disk.YandexDisk.upload_files(disk.disk_token, disk1)
