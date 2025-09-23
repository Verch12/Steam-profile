# https://a.zazaza.me/

import requests
import re
import json
import os

# <span class="pages-count">28</span>
# <a href="/da__ia_sakamoto__a_chto_/vol1/2" class="btn btn-outline-primary long mt-3 hide next-button-web">Дальше <i class="fa fa-arrow-right"></i></a>
# <img class="manga-img_0 manga-img" data-page="0" src="https://one-way.work/auto/08/60/34/e003.jpg" data-original="" rh="1038" rw="728" id="mangaPicture" pagenum="0" width="728" height="1038"> pagenum, class и data-page меняется
# 1 https://a.zazaza.me/da__ia_sakamoto__a_chto_/vol1/1#
# 2 https://a.zazaza.me/da__ia_sakamoto__a_chto_/vol1/1#page=1


"""
<script type="text/javascript">
  var prevLink = false;
  var prevChapterLink = "/da__ia_sakamoto__a_chto_"
  var nextLink = true;
  var nextChapterLink = "/da__ia_sakamoto__a_chto_/vol1/2";
  var chapterInfo = {'id': 6112, 'type': 'MANGA', 'vol': 1, 'num': 10, 'siteId': '1'};
  rm_h.readerInit(chapterInfo, [['https://one-way.work/','',"auto/08/60/34/e003.jpg?t=1758513576&u=0&h=i8KpQk0Uw7TeqnGgsGROIg",728,1038],['https://one-way.work/','',"auto/08/60/34/e004.jpg?t=1758513576&u=0&h=PJtxxMVvModXO5qqMHV6jg",728,1044],['https://one-way.work/','',"auto/08/60/34/e005.jpg_res.jpg?t=1758513576&u=0&h=J9EKU8a7dywPT94nu48QJw",728,1046],['https://one-way.work/','',"auto/08/60/34/e006.jpg_res.jpg?t=1758513576&u=0&h=LYBll3la1nGkS-iljUB7_Q",728,1043],['https://one-way.work/','',"auto/08/60/34/e007.jpg_res.jpg?t=1758513576&u=0&h=6_0TpTTBeKwV1PiR6Q346Q",728,1049],['https://one-way.work/','',"auto/08/60/34/e008.jpg_res.jpg?t=1758513576&u=0&h=9XrJaEV-P9mNmXfNHCHx-A",728,1047],['https://one-way.work/','',"auto/08/60/34/e009.jpg_res.jpg?t=1758513576&u=0&h=H7ERe94n_w4QAbcVFFBL2w",728,1031],['https://one-way.work/','',"auto/08/60/34/e010.jpg_res.jpg?t=1758513576&u=0&h=ok-H0arhQsL6stRH8vJSvg",728,1065],['https://one-way.work/','',"auto/08/60/34/e011.jpg_res.jpg?t=1758513576&u=0&h=rEnL91VT2ZtsqIX-AaeX4g",728,1037],['https://one-way.work/','',"auto/08/60/34/e012.jpg_res.jpg?t=1758513576&u=0&h=imCC1vKrigbs2a1Q1tHPQg",728,1051],['https://one-way.work/','',"auto/08/60/34/e013.jpg_res.jpg?t=1758513576&u=0&h=uJsMzoI0-CpkN2cWNUdX1Q",728,1036],['https://one-way.work/','',"auto/08/60/34/e014.jpg_res.jpg?t=1758513576&u=0&h=AhPcTWLcznGH3HWsULaTRQ",728,1056],['https://one-way.work/','',"auto/08/60/34/e015.jpg_res.jpg?t=1758513576&u=0&h=kqEUSC-hjr0tF2bTtbc-_Q",728,1054],['https://one-way.work/','',"auto/08/60/34/e016.jpg_res.jpg?t=1758513576&u=0&h=MmbHaTBqWTkIZVNizksiqg",728,1046],['https://one-way.work/','',"auto/08/60/34/e017.jpg_res.jpg?t=1758513576&u=0&h=vTg4dtCvhMV3ZttQQeP52A",728,1057],['https://one-way.work/','',"auto/08/60/34/e018.jpg_res.jpg?t=1758513576&u=0&h=H2SeJnbc7F_rd-IwGsNigQ",728,1049],['https://one-way.work/','',"auto/08/60/34/e019.jpg_res.jpg?t=1758513576&u=0&h=JxqX-5k5nrj1U011bqEgaw",728,1051],['https://one-way.work/','',"auto/08/60/34/e020.jpg_res.jpg?t=1758513576&u=0&h=gFjRFP1Mn1IY9567qGPZXg",728,1042],['https://one-way.work/','',"auto/08/60/34/e021.jpg_res.jpg?t=1758513576&u=0&h=WPXoK0MxznzAAxaiItqsUg",728,1029],['https://one-way.work/','',"auto/08/60/34/e022.jpg_res.jpg?t=1758513576&u=0&h=_dBURLWjKS7Y5wZkizX0DA",728,1044],['https://one-way.work/','',"auto/08/60/34/e023.jpg_res.jpg?t=1758513576&u=0&h=VK8YrKqp3s4yERkmhoIIhw",728,1036],['https://one-way.work/','',"auto/08/60/34/e024.jpg_res.jpg?t=1758513576&u=0&h=tQxYyTWm34ZUxdA3WM3wwg",1456,1052],['https://one-way.work/','',"auto/08/60/34/e025.jpg_res.jpg?t=1758513576&u=0&h=i8D__El4HL0fDSX9mQwC_Q",728,1045],['https://one-way.work/','',"auto/08/60/34/e026.jpg_res.jpg?t=1758513576&u=0&h=-zGUnjclU7gVf8JsmZoa6w",728,1045],['https://one-way.work/','',"auto/08/60/34/e027.jpg_res.jpg?t=1758513576&u=0&h=aIvkoW30Eu8UfkCZirfcKw",728,1058],['https://one-way.work/','',"auto/08/60/34/e028.jpg?t=1758513576&u=0&h=g2vRsZVnSE6O5BrVkHj8fA",728,1027],['https://one-way.work/','',"auto/08/60/34/e029.jpg?t=1758513576&u=0&h=_yyclGsYlM8RBr8Rjnun9g",728,1043]], false, [{"path":"https://one-way.work/","res":false}], false);
</script>
"""


url = "https://a.zazaza.me/da__ia_sakamoto__a_chto_/vol3/17"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/116.0.5845.140 Safari/537.36'
}
chapter = 8
folder_path = "src2/"

response = requests.get(url, headers=headers)
if response.status_code == 200:
    html = response.text

    match1 = re.search(r'var nextChapterLink\s*=\s*(\".*?\");', html, re.DOTALL)
    match = re.search(r'rm_h\.readerInit\([^,]+,\s*(\[\[.*?\]\])', html, re.DOTALL)

    if match1:
        js_object = match1.group(1)
        nextUrl = json.loads(js_object)
        print(f'<Response [{response.status_code}]> {url} | next: https://a.zazaza.me{nextUrl}')
    else:
        print("nextUrl не найден")

    if match:
        array_str = match.group(1)

        # немного подправляем строку для JSON
        array_str = array_str.replace("'", '"')  # одинарные кавычки → двойные
        array_str = re.sub(r',\s*false', ', null', array_str)  # false → null если нужно JSON

        # конвертируем в Python-список
        try:
            data = json.loads(array_str)
            for item in data:
                full_url = (item[0] + item[2]).split('?')[0]
                width = item[3]
                height = item[4]
                #print(f"URL: {full_url}, Width: {width}, Height: {height}")
                #print(f"{re.search(r'\d+', url.split("/")[-2]).group()}_{url.split("/")[-1]}_{data.index(item)}.jpg")

                requestsImeg = requests.get(full_url)

                if requestsImeg.status_code == 200:
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    with open(folder_path + f"{re.search(r'\d+', url.split("/")[-2]).group()}_{url.split("/")[-1]}_{data.index(item)}.jpg", "wb") as f:
                        f.write(requestsImeg.content)
                    print(f"Изображение успешно сохранено: URL: {full_url}, Width: {width}, Height: {height}.")
                else:
                    print(f"Ошибка: статус {requestsImeg.status_code}")

        except json.JSONDecodeError as e:
            print("Ошибка JSON:", e)
    else:
        print("Массив изображений не найден")