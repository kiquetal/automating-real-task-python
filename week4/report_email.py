#!/usr/bin/env python3
import os
import reports
from datetime import date
data = "/supplier-data/descriptions"

def getlines():
    text_lines = []
    cwd = os.getcwd()
    descriptions = os.listdir(cwd+data)
    for description in descriptions:
        with open(cwd+  data+"/"+description, 'r') as f:
            lines_in_description=[line.strip() for line in f.readlines()]
            text_lines.append(f"name: {lines_in_description[0]}<br/>weight: {lines_in_description[1]}\n")
    return text_lines
if __name__ == "__main__":
    tittle = "Pocessed Update on {}\n".format(date.today().strftime("%B %d, %Y"))
    filename = "/tmp/processed.pdf"
    #getlines()
    data = "<br/><br/>".join(getlines())
    print(data)
