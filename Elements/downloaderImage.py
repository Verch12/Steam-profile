# https://mangabuff.ru/

import requests
import re
import os


def  Download(url, folder_path):
    match = re.search(r'^(.*?)/([^/]+)/([^/]+)/([^/]+)\.([^./]+)$', url)
    if match:
        base, a, b, c, ext = match.groups()
        a, b, c = map(float, (a, b, c))

    try:
        b_float = float(b)
        if b_float.is_integer():
            b = str(int(b_float))
        else:
            b = str(b_float)
    except ValueError:
        pass

    for i in range(1, int(c)+1):
        url = f"{base}/{int(a)}/{b}/{i}.{ext}"
        filename = f"{int(a)}_{b}_{i}.jpg"

        response = requests.get(url)

        if response.status_code == 200:
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            with open(folder_path+filename, "wb") as f:
                f.write(response.content)
            print(f"Изображение успешно сохранено: {base}/{int(a)}/{b}/{i}.{ext}.")
        else:
            print(url)
            print(f"Ошибка: статус {response.status_code}")

if __name__ == "__main__":
    urlWebsite = input("Введите сылку на последнюю картинку с мангой в главе: ")
    Download(urlWebsite, "../Detail/JPG/")
# https://c3.mangabuff.ru/img2/chapters/kage-no-jitsuryokusha-ni-naritakute/3/10.1/22.jpg