#! /usr/bin/python3

import os
import requests

directory = "/data/feedback"
feedbacks = []
files = os.listdir(directory)
for f in files:
    with open(directory+"/"+f) as fil:
        lines = fil.readlines()
        feedbacks.append({"title":lines[0],"name":lines[1],"date":lines[2],"feedback":lines[3]})

for feedback in feedbacks:
    response = requests.post("http://34.132.98.211/feedback/",data=feedback)
    response.raise_for_status()

