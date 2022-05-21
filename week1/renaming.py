#!/usr/bin/python3

import os
from PIL import Image
directory_to_save = "/opt/icons"
directory_to_read = "/images"

cwd = os.getcwd()


images = os.listdir(cwd+directory_to_read)
size = (128,128)
for image in images:
    if not image.startswith("."):
        im = Image.open(cwd+directory_to_read+"/"+image)
        if im.mode != "RGB":
            im = im.convert("RGB")
        im = im.rotate(270)
        im = im.resize(size)
        im.save(directory_to_save+"/"+image,"JPEG")

