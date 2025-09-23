from PIL import Image

def cropJPG(path, output_path):
    img = Image.open(path)
    width, height = img.size

    parts = 5
    part_width = width // parts

    for i in range(parts):
        left = i * part_width
        right = (i + 1) * part_width if i < parts - 1 else width  # последний кусок — до конца
        cropped = img.crop((left, 0, right, height))
        cropped.save(f"{output_path}/part_{i+1}.jpg")
        print(f"Сохранено: part_{i+1}.jpg")
    print("✅ Готово: PARTS")

if __name__ == "__main__":
    img = input("Название файла в папке Intermediat: ")
    if img[-4:] != ".jpg":
        img = img + ".jpg"
    cropJPG(f"Intermediate/{img}", "../Part")