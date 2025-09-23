from PIL import Image

# Открываем изображение
img = Image.open("output1.jpg")
width, height = img.size

# Количество частей
parts = 5
part_width = width // parts

# Разрезаем и сохраняем
for i in range(parts):
    left = i * part_width
    right = (i + 1) * part_width if i < parts - 1 else width  # последний кусок — до конца
    cropped = img.crop((left, 0, right, height))
    cropped.save(f"part_{i+1}.jpg")
    print(f"Сохранено: part_{i+1}.jpg")