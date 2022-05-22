#! /usr/bin/env python3
import os
import requests
directory_to_read = "/supplier-data/images/"
cwd = os.getcwd()
images = os.listdir(cwd+directory_to_read)
for image in images:
    if (image.endswith(".jpeg")):
        print(image)
        with open(cwd+directory_to_read+image, "rb") as image_file:
            print(image_file)
            r = requests.post("http://localhost/upload/", files={"file": image_file})
            print(r.status_code)
~
~
