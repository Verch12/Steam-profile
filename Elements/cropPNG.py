from PIL import Image

def cropPNG(path):
    Image.MAX_IMAGE_PIXELS = None
    #img = Image.open("Intermediate/output.png")

    width, height = path.size
    num_parts = 5
    part_width = width // num_parts

    for i in range(num_parts):
        left = i * part_width
        right = (i + 1) * part_width
        if i == num_parts - 1:
            right = width
        part = path.crop((left, 0, right, height))
        part.save(f"Part/part_{i+1}.png")

if __name__ == "__main__":
    img = input("Название файла в папке Intermediat: ")
    if img[-4:] != ".png":
        img = img + ".png"
    cropPNG(f"Intermediate/{img}")