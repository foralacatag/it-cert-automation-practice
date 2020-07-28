#!/usr/bin/env python3
import datetime
import os
import requests
import emails
from datetime import datetime
import run


if __name__ == "__main__":
     title="Processed Update on" + datetime.today().strftime('%Y-%m-%d')
     list=run.data_dict()
     for elem in list:
       paragah="name: {}\nweight: {} lbs".format(elem["name"], elem["weight"])
       reports.generate_report("/tmp/processed.pdf", title, paragrah)

sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
subject = "Upload Completed - Online Fruit Store"
body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email"

message = emails.generate(sender, receiver, subject, body, "/tmp/processed.pdf")
emails.send(message)
