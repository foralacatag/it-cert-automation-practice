#!/usr/bin/env python3
import requests
import os
# This example shows how a file can be uploaded using
# The Python Requests module
home="/home/student-00-f3438403c3f4/supplier-data/images/"
os.chdir(home)
arr = [f for f in os.listdir('.') if f.endswith('.jpeg')]
url = "http://localhost/upload/"
for file in arr:
  with open(file, 'rb') as opened:
    r = requests.post(url, files={'file': opened})
