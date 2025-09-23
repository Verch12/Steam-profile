# https://a.zazaza.me/

import requests
import re
import json
import os

from bs4 import BeautifulSoup


def  Download(url, folder_path, chapter):
    nextUrl = ""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/116.0.5845.140 Safari/537.36'
    }

    while chapter != 0:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            html = response.text

            matchLink = re.search(r'var nextChapterLink\s*=\s*(\".*?\");', html, re.DOTALL)
            match = re.search(r'rm_h\.readerInit\([^,]+,\s*(\[\[.*?\]\])', html, re.DOTALL)

            if matchLink:
                js_object = matchLink.group(1)
                nextUrl = f"https://a.zazaza.me{json.loads(js_object)}"
                print(f'<Response [{response.status_code}]> {url} | next: {nextUrl}')
            else:
                print("nextUrl не найден")

            if match:
                array_str = match.group(1)
                array_str = array_str.replace("'", '"')
                array_str = re.sub(r',\s*false', ', null', array_str)
                #print(len(json.loads(array_str)))

                try:
                    data = json.loads(array_str)
                    for item in data:
                        full_url = (item[0] + item[2]).split('?')[0]
                        width = item[3]
                        height = item[4]

                        requestsImeg = requests.get(full_url)

                        if requestsImeg.status_code == 200:
                            if not os.path.exists(folder_path):
                                os.makedirs(folder_path)
                            with open(f"{folder_path}{re.search(r'\d+', url.split("/")[-2]).group()}_{url.split("/")[-1]}_{data.index(item)}.jpg", "wb") as f:
                                f.write(requestsImeg.content)
                            print(f"Изображение успешно сохранено: URL: {full_url}, Width: {width}, Height: {height}.")
                            #print(f"Path: {folder_path}{re.search(r'\d+', url.split("/")[-2]).group()}_{url.split("/")[-1]}_{data.index(item)}.jpg")
                        else:
                            print(f"Ошибка: статус {requestsImeg.status_code}")

                except json.JSONDecodeError as e:
                    print("Ошибка JSON:", e)
            else:
                print("Массив изображений не найден")

        url = nextUrl
        chapter -= 1
        if chapter != 0: print(f"Next URL ---> {nextUrl}\n")


# https://a.zazaza.me/da__ia_sakamoto__a_chto_/vol1/1
if __name__ == "__main__":
    urlWebsite = input("Введите сылку на сайт с мангой: ")
    chapter = int(input("Введите число последующих глав на скачивание: "))
    Download(urlWebsite, "../Detail/PNG/", chapter)