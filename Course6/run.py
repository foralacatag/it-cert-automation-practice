#! /usr/bin/env python3
import json
import os
import requests

#list comprehension for all text files
files=[f for f in os.listdir('/data/feedback') if f.endswith('.txt')]

#with open('people.json', 'w') as people_json:
#    json.dump(files, people_json, indent=2)
#change directory to current one
os.chdir("/data/feedback/")

#print(files)

#list to hold each dictionary  from each file
list=[]
titles=["title", "name", "date", "feedback"]

#iterate over each file to add it to the list
for file in files:
    dict1={}
    with open(file) as fh: 
        command=0
        for line in fh: 
  
            # reads each line and trims of extra the spaces  
            # and gives only the valid words 
            
            description = line.strip()
            dict1[titles[command]] = description.strip() 
            command+=1
    list.append(dict1)
#print(list)

#post each dictionary to website feedback page
for elem in list:
    #p={"title": elem["title"], "name":elem["name"], "date":elem["date"], "feedback":elem["feedback"]}
    response = requests.post("http://35.238.69.203/feedback/", data=elem)
    print(response.status_code)
