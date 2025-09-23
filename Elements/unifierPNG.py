from PIL import Image
import os

def Сombination(folder_path, output_path):
    files = [f.replace(".jpg","") for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    sorted_files = sorted(files, key=lambda x: tuple(float(n) for n in x.split('_')))

    new_width = 750

    images = []
    for path in sorted_files:
        print(path)
        img = Image.open(folder_path + path + ".jpg")

        w_percent = new_width / img.width
        new_height = int(img.height * w_percent)
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)

        images.append(resized_img)

    total_height = sum(img.height for img in images)
    final_width = new_width
    final_height = total_height
    combined = Image.new("1", (final_width, final_height), color=1)

    y_offset = 0
    for img in images:
        combined.paste(img, (0, y_offset))
        y_offset += img.height

    combined.save(output_path, optimize=True)
    print("✅ Готово: output.png")

if __name__ == '__main__':
    Сombination("../Detail/PNG/", "../Intermediate/output.png")