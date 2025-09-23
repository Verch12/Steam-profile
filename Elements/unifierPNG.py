from PIL import Image

# width, height = 150, 279_620
# img = Image.new("1", (width, height), color=1)
# img.save("output_150x279620_1bit.png", optimize=True)

import os

folder_path = "src2/"
files = [f.replace(".jpg","") for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
sorted_files = sorted(files, key=lambda x: tuple(map(int, x.split('_'))))

new_width = 750

# Открываем и масштабируем изображения
images = []
for path in sorted_files:
    print(path)
    img = Image.open(folder_path + path + ".jpg")

    # Пропорциональное уменьшение по ширине
    w_percent = new_width / img.width
    new_height = int(img.height * w_percent)
    resized_img = img.resize((new_width, new_height), Image.LANCZOS)

    images.append(resized_img)

# Вычисляем итоговые размеры
total_height = sum(img.height for img in images)
final_width = new_width
final_height = total_height

# Создаём холст
combined = Image.new("1", (final_width, final_height), color=1)

# Склеиваем вертикально
y_offset = 0
for img in images:
    combined.paste(img, (0, y_offset))
    y_offset += img.height

# Сохраняем
combined.save("output.png", optimize=True)
print("✅ Готово: output.png")
