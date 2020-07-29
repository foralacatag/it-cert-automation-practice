#! /usr/bin/env python3
import os
import requests
import re
import json
import pathlib


#print(files)

def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


#list to hold each dictionary  from each file
def data_dict():
  home="/home/student-02-a6b22d3abcd6/supplier-data/descriptions/"
  os.chdir(home)
  files = [f for f in os.listdir('.') if f.endswith('.txt')]
  sorted(files)
  list=[]
  titles=["name", "weight", "description"]

  #iterate over each file to add it to the list
  for file in files:
    command=0
    print(file, command)
    dict1={}
    with open(file) as fh:
      for line in fh:
            # reads each line and trims of extra the spaces
            # and gives only the valid words
        description = line.strip()
        if command == 1:
          dict1[titles[command]]=int(re.split('[\s,]+', description)[0])
        else:
          dict1[titles[command]] = description.strip()
        command+=1
        if command>=3:
          break
    dict1["image_name"]=os.path.basename(file).split(".")[0]+".jpeg"

    print(dict1)
    #Added creating text files with names and weights
    with open("/home/student-02-a6b22d3abcd6/report.txt", 'a') as file:
      file.write("name: {}\nweight: {} lbs\n".format(dict1["name"], dict1["weight"])   )
    list.append(dict1)
  return list

#add list to json file
#with open('fruits.json', 'w') as fruit_json:
#    json.dump(list, fruit_json, indent=2)


#Post each dictionary element to the website
url = "http://35.232.202.143/fruits/"
#with open("fruits.json", 'rb') as opened:

list=data_dict()
#print(list)
for elem in list:
  d={"name":elem["name"], "weight":elem["weight"], "description":elem["description"], "image_name":elem["image_name"]}
  r = requests.post(url, data=d)
  print(r.status_code)
