from PIL import Image

Image.MAX_IMAGE_PIXELS = None
# открываем исходное изображение
img = Image.open("output.png")

width, height = img.size
num_parts = 5
part_width = width // num_parts

for i in range(num_parts):
    left = i * part_width
    right = (i + 1) * part_width
    # на случай, если ширина не делится нацело
    if i == num_parts - 1:
        right = width
    part = img.crop((left, 0, right, height))
    part.save(f"part/part_{i+1}.png")
