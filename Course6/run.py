#! /usr/bin/env python3
import os
import requests
import re
import json


print(files)

def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


#list to hold each dictionary  from each file
def data_dict():
  home="/home/student-00-f3438403c3f4/supplier-data/descriptions/"
  os.chdir(home)
  files = [f for f in os.listdir('.') if f.endswith('.txt')]
  sorted(files)
  list=[]


  titles=["name", "weight", "description", "image_name"]

#iterate over each file to add it to the list
  for file in files:
    with open(file) as fh:
      command=0 
      dict1={}
      dict1[titles[3]]=os.path.basename(file[:-4])+".jpeg"
      for line in fh:
            # reads each line and trims of extra the spaces
            # and gives only the valid words
        description = line.strip()
        if command == 1:
          dict1[titles[command]]=int(re.split('[\s,]+',description)[0])
        else:
          dict1[titles[command]] = description.strip()
        command+=1
    #print(dict1)
    list.append(dict1)
  return list

#add list to json file
with open('fruits.json', 'w') as fruit_json:
    json.dumps(list, fruit_json, indent=2)


#Post each dictionary element to the website
url = "http://localhost/fruits/"
#with open("fruits.json", 'rb') as opened:
elem=load_data(data_dict())
print(elem)
r = requests.post(url, data=elem)
print(r.status_code)

