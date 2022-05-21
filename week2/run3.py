#!/usr/bin/python3
import os
import requests

directory = "/data/feedback"
feedbacks = []
files = os.listdir(directory)
for f in files:
    if not f.endswith(".txt"):
        continue
    with open(directory+"/"+f) as fil:
        lines = [i.strip() for i in fil.readlines()]
        feedback={"title":lines[0].strip(),"name":lines[1].strip(),"date":lines[2].strip(),"feedback":lines[3].strip()}
        response = requests.post("http://34.70.50.116/feedback/",json=feedback)
        response.raise_for_status()
        print(response.request.body)
        print(response.status_code)
~                                   
