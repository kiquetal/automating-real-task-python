#! /usr/bin/env python3
import requests
import os
from pathlib import Path
directory_to_read="/supplier-data/descriptions"

cwd = os.getcwd()

descriptions = os.listdir(cwd+directory_to_read)

for description in descriptions:
    json_file={}
    with open(cwd+directory_to_read+"/"+description) as desc:
        alist = desc.read().split("\n")
        weight = alist[1].split()[0]
        json_file={'name':alist[0],'weight':int(weight),'description':alist[2],'image_name':Path(description).stem+".jpeg"}
        r = requests.post("http://35.239.101.215/fruits/",json=json_file)
