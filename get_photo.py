import requests
from bs4 import BeautifulSoup
from time import sleep


def get_photo(url: str):
    content = requests.get(url,
                           headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) '
                                                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 '
                                                  'Safari/537.36'})
    page = BeautifulSoup(content.content, "html.parser")
    img_comp = page.find("section", class_="comp")
    if img_comp == None:
        return False

    print(img_comp.find("picture").find("img").get("src").split("?")[0])
    return img_comp.find("picture").find("img").get("src").split("?")[0]


def get_url_photo(name: str):
    content = requests.get(f"https://unsplash.com/s/photos/{name}",
                           headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) '
                                                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 '
                                                  'Safari/537.36'})
    page = BeautifulSoup(content.content, "html.parser")
    imagion = page.find("body").find("div").find("div", class_="NTfdD").find_all("a")
    url = []
    for img_figure in imagion:
        url.append(get_photo(img_figure.get("href")))
    return url
