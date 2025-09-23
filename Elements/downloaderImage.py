# https://mangabuff.ru/

import requests
import os

a = int(input())
b = int(input())
c = int(input())

for i in range(1, c+1):
    folder_path = "src/"
    #url = f"https://c3.mangabuff.ru/img2/chapters/kage-no-jitsuryokusha-ni-naritakute/{a}/{b}/{i}.jpg"  # Замените на нужную ссылку
    url = f"https://c3.mangabuff.ru/img2/chapters/heugmag-eul-beolineun-desilpaehaessda/{a}/{b}/{i}.jpeg"
    filename = f"{a}_{b}_{i}.jpg"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        with open(folder_path+filename, "wb") as f:
            f.write(response.content)
        print(f"Изображение успешно сохранено: {i}.")
    else:
        print(url)
        print(f"Ошибка: статус {response.status_code}")