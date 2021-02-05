import os
import re

from PIL import Image


def background_to_transparent(img_path, img_name, save_path):
    img = Image.open(img_path)
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    img.putdata(newData)
    img.save(save_path + img_name, "PNG")


images_folder = "D:\\data\\temp\\coverage\\pci\\"
new_folder = f"{images_folder}\\result"
os.makedirs(new_folder)
for img in os.listdir(images_folder):
    if re.match(r".*(jpg|jpeg|gif|png)", img):
        img_path = images_folder + img
        background_to_transparent(img_path, img, images_folder)
