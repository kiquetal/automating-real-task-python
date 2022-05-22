#! /usr/bin/env python3
import os
from PIL import Image
from pathlib import Path


directory_to_read="/supplier-data/images"
cwd = os.getcwd()
images = os.listdir(cwd+directory_to_read)
for image in images:
    if (image.endswith(".tiff")):
        im = Image.open(cwd+directory_to_read+"/"+image)
        if im.mode !="RGB":
            im = im.convert("RGB")
        im = im.resize((600,400))
        name = Path(cwd+directory_to_read+"/"+image).stem
        im.save(cwd+directory_to_read+"/"+name+".jpeg","JPEG")

