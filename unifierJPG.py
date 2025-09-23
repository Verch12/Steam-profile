from PIL import Image
import os

folder_path = "src/"
files = [f.replace(".jpg","") for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
sorted_files = sorted(files, key=lambda x: tuple(map(int, x.split('_'))))

new_width = 750
MAX_HEIGHT = 65500

# Открываем и масштабируем изображения
images = []
for path in sorted_files:
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

# Если превышает лимит — пересчитай всё
if total_height > MAX_HEIGHT:
    print(f"⚠️ Высота {total_height} превышает {MAX_HEIGHT}, уменьшаем...")

    # Коэффициент сжатия по высоте
    scale_ratio = MAX_HEIGHT / total_height
    final_height = 0
    for i in range(len(images)):
        img = images[i]
        new_h = int(img.height * scale_ratio)
        images[i] = img.resize((final_width, new_h), Image.LANCZOS)
        final_height += new_h

# Создаём холст
combined = Image.new("RGB", (final_width, final_height))

# Склеиваем вертикально
y_offset = 0
for img in images:
    combined.paste(img, (0, y_offset))
    y_offset += img.height

# Сохраняем
combined.save("output1.jpg")
print("✅ Готово: output1.jpg")
